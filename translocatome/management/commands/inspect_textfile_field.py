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

            field_no = 17
            print 'Field name: ', header[field_no]

            kinds = {}
            for line in input_file.readlines():
                processed_line = self.parse_line(line)
                values = processed_line[field_no].split('|')
                for raw_value in values:
                    value = raw_value.strip()
                    if value in kinds.keys():
                        kinds[value] += 1
                    else:
                        kinds[value] = 1
                # try:
                #     value = processed_line[field_no]
                #     if value in kinds.keys():
                #         kinds[value] += 1
                #     else:
                #         kinds[value] = 1
                # except:
                #     pass
            kind_keys = kinds.keys()
            kind_keys.sort()
            for kind in kind_keys:
                print kind, ' : ', kinds[kind]
