import pprint

from optparse import make_option

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    option_list = BaseCommand.option_list + (
        make_option('--input_file_name'),
    )

    @staticmethod
    def parse_line(line):
        return line.strip().split('\t')

    def handle(self, *args, **options):
        file_name = options['input_file_name']

        with open(file_name, 'r') as input_file:
            header = self.parse_line(input_file.readline())

            fields = {}
            for column_name in header:
                fields[column_name] = {}

            for line in input_file.readlines():
                processed_line = self.parse_line(line)

                for field_no in range(len(processed_line)):
                    values = processed_line[field_no].split('|')
                    kinds = {}

                    for raw_value in values:
                        value = raw_value.strip()
                        if value in kinds.keys():
                            kinds[value] += 1
                        else:
                            kinds[value] = 1

                    for kind in kinds:
                            fields[header[field_no]][kind] = fields[header[field_no]].get(kind, 0) + kinds[kind]
            pp = pprint.PrettyPrinter(indent=4)
            del fields['UniProtAC']
            pp.pprint(fields)
