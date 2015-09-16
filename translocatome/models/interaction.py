from django.db import models

from .node import Node
from .metadata import MetaData

from translocatome.input_tranlations import RAW_EFFECT_VALUE_BOTH, RAW_EFFECT_VALUE_UNKNOWN, BIOLOGICAL_PROCESSES_VALUES


class InteractionSubtype(models.Model):
    value = models.CharField(max_length=100)


class InteractionType(models.Model):
    value = models.CharField(max_length=100)
    subtype = models.ManyToManyField(InteractionSubtype)


BIOLOGICAL_PROCESS_VALUE_APOPTOSIS = 0
BIOLOGICAL_PROCESS_VALUE_CRI = 1
BIOLOGICAL_PROCESS_VALUE_DDR = 2
BIOLOGICAL_PROCESS_VALUE_HYPOXIA = 3
BIOLOGICAL_PROCESS_VALUE_MAPK = 4
BIOLOGICAL_PROCESS_VALUE_PLC = 5
BIOLOGICAL_PROCESS_VALUE_PROLIF = 6

BIOLOGICAL_PROCESS_VALUES = (
    (BIOLOGICAL_PROCESS_VALUE_APOPTOSIS, 'apoptosis'),
    (BIOLOGICAL_PROCESS_VALUE_CRI, 'cri'),
    (BIOLOGICAL_PROCESS_VALUE_DDR, 'ddr'),
    (BIOLOGICAL_PROCESS_VALUE_HYPOXIA, 'hypoxia'),
    (BIOLOGICAL_PROCESS_VALUE_MAPK, 'mapk'),
    (BIOLOGICAL_PROCESS_VALUE_PLC, 'plc'),
    (BIOLOGICAL_PROCESS_VALUE_PROLIF, 'prolif'),
)


class BiologicalProcess(models.Model):
    value = models.SmallIntegerField(choices=BIOLOGICAL_PROCESS_VALUES)


EDGE_TYPES_VALUES = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
)

DIRECTNESS_DIRECT = 0
DIRECTNESS_INDIRECT = 1
DIRECTNESS_UNKNOWN = 2
DIRECTNESS_DIRECT_AND_INDIRECT = 3

DIRECTNESS_VALUES = (
    (DIRECTNESS_DIRECT, 'direct'),
    (DIRECTNESS_INDIRECT, 'indirect'),
    (DIRECTNESS_UNKNOWN, 'unknown'),
    (DIRECTNESS_DIRECT_AND_INDIRECT, 'direct_and_indirect')
)

EFFECT_VALUE_FLOAT = 0
EFFECT_VALUE_UNKNOWN = 1
EFFECT_VALUE_BOTH = 2

EFFECT_VALUE_TYPES = (
    (EFFECT_VALUE_FLOAT, 'float'),
    (EFFECT_VALUE_UNKNOWN, 'unknown'),
    (EFFECT_VALUE_BOTH, 'both'),
)

class EffectValue(models.Model):
    type = models.SmallIntegerField(choices=EFFECT_VALUE_TYPES)
    value = models.FloatField(null=True)

    @staticmethod
    def create_object_from_raw_data(raw_data):
        stripped_data = raw_data.strip()
        try:
            value = float(stripped_data)
            effect_value_object = EffectValue(type=EFFECT_VALUE_FLOAT, value=value)

        except ValueError:
            if stripped_data == RAW_EFFECT_VALUE_BOTH:
                effect_type = EFFECT_VALUE_BOTH
            elif stripped_data == RAW_EFFECT_VALUE_UNKNOWN:
                effect_type = EFFECT_VALUE_UNKNOWN
            else:
                raise ValueError

            effect_value_object = EffectValue(type=effect_type)
        effect_value_object.save()
        return effect_value_object


class Interaction(models.Model):
    source_node = models.ForeignKey(Node, related_name='source')
    target_node = models.ForeignKey(Node, related_name='target')

    meta_data = models.ForeignKey(MetaData)

    # TODO @fodma1: Make a use of interaction type! Discuss the details with Dani!
    interaction_type = models.CharField(max_length=100)
    edge_type = models.PositiveSmallIntegerField(choices=EDGE_TYPES_VALUES)
    directness = models.PositiveSmallIntegerField(choices=DIRECTNESS_VALUES)
    effect_all = models.ForeignKey(EffectValue, related_name='effect_all')
    effect_final = models.ForeignKey(EffectValue, related_name='effect_final')
    biological_process = models.ManyToManyField(BiologicalProcess)
    score = models.SmallIntegerField(null=True)

    # might not needed in the future
    int_abrev = models.CharField(max_length=13)
    # rename to total?
    is_in_full = models.BooleanField(default=False)
    is_in_medium = models.BooleanField(default=False)
    is_in_small = models.BooleanField(default=False)
    is_in_skeleton = models.BooleanField(default=False)

    def add_biological_process(self, raw_data):
        process_names = [raw_entry.strip() for raw_entry in raw_data.split('|')]

        process_objects = []

        for process_name in process_names:
            if process_name == 'N/A':
                continue

            try:
                process = BiologicalProcess.objects.get(value=BIOLOGICAL_PROCESSES_VALUES[process_name])
                # TODO @fodma1: Use something more specific than Exception eg. DoesNotExists
            except Exception:
                process = BiologicalProcess(value=BIOLOGICAL_PROCESSES_VALUES[process_name])
                process.save()

            process_objects.append(process)

        self.biological_process.add(*process_objects)
        self.save()

    def add_score_value(self, raw_data):
        data = raw_data.strip()
        try:
            number = int(data)
        except ValueError:
            return
        self.score = number
        self.save()

    def add_network_flags(self, data):
        self.is_in_full = '#FULL' in data and data['#FULL'].strip() == '#FULL'
        self.is_in_medium = '#MEDIUM' in data and data['#MEDIUM'].strip() == '#MEDIUM'
        self.is_in_small = '#SMALL' in data and data['#SMALL'].strip() == '#SMALL'
        self.is_in_skeleton = '#SIG' in data and data['#SIG'].strip() == '#SIG'

        self.save()

    def get_list_object(self):
        biological_processes = ' | '.join([dict(BIOLOGICAL_PROCESS_VALUES)[biological_process['value']] for biological_process in self.biological_process.all().values()])
        return {
            'interaction_type': self.interaction_type,
            'edge_type': str(self.edge_type),
            'directness': dict(DIRECTNESS_VALUES)[self.directness],
            'biological_process': biological_processes,
            'score': str(self.score),
            'is_in_full': self.is_in_full,
            'is_in_medium': self.is_in_medium,
            'is_in_small': self.is_in_small,
            'is_in_skeleton': self.is_in_skeleton,
            'meta': {
                'entry_state': self.meta_data.get_entry_state(),
                'reviewed': self.meta_data.reviewed,
            },
        }
