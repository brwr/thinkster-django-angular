from rest_framework import serializers
from translocatome.models import Node

class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Node
        fields = ('id', 'uni_prot_ac', 'gene_name', 'base_activity', 'base_concentration', 'cancer_driver', 'cancer_indirect_driver')
