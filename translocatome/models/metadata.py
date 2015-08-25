from django.db import models

from authentication.models import Account

from translocatome.input_tranlations import SOURCES_VALUES, REFERENCE_VALUE_MANUAL_CURATION, DATA_SOURCE_TRANSLATIONS

class Source(models.Model):
    value = models.CharField(max_length=32)


REFERENCE_TYPE_PUBMED = 0
REFERENCE_TYPE_BOOK = 1
REFERENCE_TYPE_MANUAL = 2

REFERENCE_TYPES = (
    (REFERENCE_TYPE_PUBMED, 'pubmed'),
    (REFERENCE_TYPE_BOOK, 'book'),
    (REFERENCE_TYPE_MANUAL, 'manual'),
)

class Reference(models.Model):
    reference_type = models.SmallIntegerField(choices=REFERENCE_TYPES)
    value = models.CharField(max_length=50)

DATA_SOURCE_VALUE_BASE_PPI = 0
DATE_SOURCE_VALUE_MANUAL_CURATION = 1
DATA_SOURCE_TYPE_SIGNALING_POOL = 2

DATA_SOURCE_VALUES = (
    (DATA_SOURCE_VALUE_BASE_PPI, 'base_ppi'),
    (DATE_SOURCE_VALUE_MANUAL_CURATION, 'manual_curation'),
    (DATA_SOURCE_TYPE_SIGNALING_POOL, 'signaling_pool'),
)


class DataSource(models.Model):
    value = models.SmallIntegerField(choices=DATA_SOURCE_VALUES)

ENTRY_STATE_INTEGRATED = 0
ENTRY_STATE_MANUALLY_REVIEWED = 1
ENTRY_STATE_DELETED = 2
ENTRY_STATE_REWIRED = 3

ENTRY_STATE_VALUES = (
    (ENTRY_STATE_INTEGRATED, 'integrated'),
    (ENTRY_STATE_MANUALLY_REVIEWED, 'manually_rewired'),
    (ENTRY_STATE_DELETED, 'deleted'),
    (ENTRY_STATE_REWIRED, 'rewired'),
)


class MetaData(models.Model):
    data_source = models.ManyToManyField(DataSource, null=True)
    sources = models.ManyToManyField(Source)
    references = models.ManyToManyField(Reference, null=True)
    comment = models.CharField(max_length=500)
    entry_state = models.SmallIntegerField(choices=ENTRY_STATE_VALUES)
    # Make it null for now!
    curator_name = models.ForeignKey(Account, null=True)
    reviewed = models.BooleanField(default=False)
    curators_comment = models.CharField(max_length=500)

    def add_data_sources(self, raw_data):
        data_source_names = [data_source_name.strip() for data_source_name in raw_data.split('|')]

        data_source_objects = []

        for data_source_name in data_source_names:
            if data_source_name == 'NA':
                continue

            try:
                data_source = DataSource.objects.get(value=DATA_SOURCE_TRANSLATIONS[data_source_name])
            except Exception:
                data_source = DataSource(value=DATA_SOURCE_TRANSLATIONS[data_source_name])
                data_source.save()

            data_source_objects.append(data_source)

        self.data_source.add(*data_source_objects)
        self.save()

    def add_sources(self, raw_data):
        source_names = [SOURCES_VALUES[source_name.strip()] for source_name in raw_data.split('|')]

        source_objects = []

        for source_name in source_names:
            try:
                source = Source.objects.get(value=source_name)
            #TODO @fodma1: Find a better Exception class!
            except Exception:
                source = Source(value=source_name)
                source.save()

            source_objects.append(source)

        self.sources.add(*source_objects)
        self.save()

    def add_references(self, raw_data):
        reference_values = [source_name.strip() for source_name in raw_data.split('|')]

        reference_objects = []

        for reference_value in reference_values:
            if reference_value.isdigit():
                try:
                    reference_object = Reference.objects.get(reference_type=REFERENCE_TYPE_PUBMED, value=reference_value)

                except Exception:
                    reference_object = Reference(reference_type=REFERENCE_TYPE_PUBMED, value=reference_value)
                    reference_object.save()

            elif reference_value.startswith('Book'):
                book_name = reference_value[reference_value.find("(")+1:reference_value.find(")")]
                try:
                    reference_object = Reference.objects.get(reference_type=REFERENCE_TYPE_BOOK, value=book_name)

                except Exception:
                    reference_object = Reference(reference_type=REFERENCE_TYPE_PUBMED, value=book_name)
                    reference_object.save()

            elif reference_value == REFERENCE_VALUE_MANUAL_CURATION:
                try:
                    reference_object = Reference.objects.get(reference_type=REFERENCE_TYPE_MANUAL)

                except Exception:
                    reference_object = Reference(reference_type=REFERENCE_TYPE_MANUAL)
                    reference_object.save()

            reference_objects.append(reference_object)

        self.references.add(*reference_objects)
        self.save()

    def get_entry_state(self):
        return dict(ENTRY_STATE_VALUES)[self.entry_state]
