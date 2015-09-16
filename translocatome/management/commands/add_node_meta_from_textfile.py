from optparse import make_option

from django.core.management.base import BaseCommand

from translocatome.input_tranlations import NODE_META_FILE_FIELD_NAME_TO_INDEX
from translocatome.models import Node

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
            updated_nodes = 0
            for raw_line in input_file.readlines():
                line = self.parse_line(raw_line)
                data = self.convert_line_to_data(line)

                nodes = Node.objects.filter(uni_prot_ac=data['UniProtAC'])

                for node in nodes:
                    try:
                        node.base_activity = float(data['Base_Activity'])
                    except:
                        pass

                    try:
                        node.base_concentration = float(data['Base_Concentration'])
                    except:
                        pass

                    try:
                        node.cancer_driver = float(data['Cancer_Driver'])
                    except:
                        pass

                    try:
                        node.cancer_indirect_driver = float(data['Cancer_Indirect_Target'])
                    except:
                        pass

                    node.save()
                    updated_nodes += 1
                counter += 1
                if counter % 10 == 0:
                    print counter

            print 'processed input lines: ', counter
            print 'updated nodes: ', updated_nodes
            print 'all nodes count: ', Node.objects.count()

    @staticmethod
    def parse_line(raw_line):
        return [element.strip() for element in raw_line.strip().split('\t')]

    @staticmethod
    def convert_line_to_data(line):
        data = {}
        for i in range(len(line)):
            data[NODE_META_FILE_FIELD_NAME_TO_INDEX[i]] = line[i]
        return data
