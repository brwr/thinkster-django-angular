from optparse import make_option

from django.core.management.base import BaseCommand

from translocatome.input_tranlations import INTERACTION_FILE_FIELD_NAME_TO_INDEX, DIRECTNESS_TRANSLATIONS, ENTRY_STATE_VALUES, REVIEWED_VALUES
from translocatome.models import Node, Interaction, MetaData
from translocatome.models.interaction import EffectValue

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    option_list = BaseCommand.option_list + (
        make_option('--input_file_name'),
    )

    def handle(self, *args, **options):
        file_name = options['input_file_name']

        with open(file_name, 'r') as input_file:
            self.parse_line(input_file.readline())

            counter = 0
            for raw_line in input_file.readlines():
                line = self.parse_line(raw_line)
                data = self.convert_line_to_data(line)

                source_node = self.get_source_node(data)

                target_node = self.get_target_node(data)

                meta = self.get_meta(data)

                self.get_interaction(data, source_node, target_node, meta)

                print counter
                counter += 1

    @staticmethod
    def parse_line(line):
        return line.strip().split('\t')

    @staticmethod
    def convert_line_to_data(line):
        data = {}
        for i in range(len(line)):
            data[INTERACTION_FILE_FIELD_NAME_TO_INDEX[i]] = line[i]
        return data

    @staticmethod
    def get_source_node(data):
        node, _ = Node.objects.get_or_create(uni_prot_ac=data['Source_UniProtAC'], gene_name=data['Source_GeneName'])
        return node

    @staticmethod
    def get_target_node(data):
        node, _ = Node.objects.get_or_create(uni_prot_ac=data['Target_UniProtAC'], gene_name=data['Target_GeneName'])
        return node

    @staticmethod
    def get_interaction(data, source_node, target_node, meta_data):
        interaction = Interaction(
            source_node=source_node,
            target_node=target_node,
            meta_data=meta_data,
            interaction_type=data['InteractionType'],
            edge_type=int(data['Edge_type']),
            directness=DIRECTNESS_TRANSLATIONS[data['Directness']],
            effect_all=EffectValue.create_object_from_raw_data(data['Effect_ALL']),
            effect_final=EffectValue.create_object_from_raw_data(data['Effect_FINAL'])
        )
        interaction.save()

        # TODO @fodma1: Make these methods on Interaction!
        interaction.add_biological_process(data['Biol_Process'])
        interaction.add_score_value(data['Score'])
        interaction.int_abrev = data['Int_Abrev'].strip()
        interaction.add_network_flags(data)

        interaction.save()
        return interaction

    @staticmethod
    def get_meta(data):
        try:
            meta = MetaData(
                entry_state=ENTRY_STATE_VALUES[data['EntryType']],
                reviewed=REVIEWED_VALUES[data['Reviewed']],
                comment=data['Comment'].decode('utf-8'),
                curators_comment=data['Personal_Comment'].decode('utf-8')
            )
            meta.save()

            meta.add_data_sources(data['DataSource'])
            meta.add_sources(data['Sources'])
            meta.add_references(data['References'])

            meta.save()
        except Exception as ex:
            print data
            raise ex
        return meta
