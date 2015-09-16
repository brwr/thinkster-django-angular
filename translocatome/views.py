from django.core import serializers
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_GET

from utils.http_response import HttpResponseJSON

from models import Interaction


@require_GET
def query_interactions(request):
    source_node_id = request.GET.get('source_node_id')
    target_node_id = request.GET.get('target_node_id')

    query_dict = {}

    if source_node_id:
        query_dict['source_node_id'] = source_node_id

    if target_node_id:
        query_dict['target_node_id'] = target_node_id

    if not query_dict:
        return HttpResponseBadRequest()

    interactions = serializers.serialize('json', Interaction.objects.filter(**query_dict), use_natural_foreign_keys=True, use_natural_primary_keys=True)

    return HttpResponseJSON(interactions)
