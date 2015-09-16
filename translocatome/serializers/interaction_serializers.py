from rest_framework import serializers
from translocatome.models import Interaction

class InteractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interaction
        fields = ('id', 'source_node', 'target_node', 'meta_data', 'interaction_type', 'edge_type', 'directness', 'effect_all', 'effect_final', 'biological_process', 'score', 'int_abrev', 'is_in_full', 'is_in_medium', 'is_in_small', 'is_in_skeleton',)
        depth = 1
