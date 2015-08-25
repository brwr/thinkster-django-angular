from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_GET

from utils.http_response import HttpResponseJSON

from models import Node, Interaction

@require_GET
def query_nodes(request):
    uni_prot_ac = request.GET.get('uni_prot_ac', '')
    gene_name = request.GET.get('gene_name', '')

    query_params = {}
    if uni_prot_ac and len(uni_prot_ac) > 2:
        query_params['uni_prot_ac__startswith'] = uni_prot_ac

    if gene_name and len(gene_name) > 2:
        query_params['gene_name__startswith'] = gene_name

    data = {'nodes': []}
    if query_params:
        data['nodes'] = Node.objects.filter(**query_params).values()

    return HttpResponseJSON(data)

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

    interactions = Interaction.objects.select_related('biological_preocess', 'meta', 'source_node', 'target_node').filter(**query_dict)

    return HttpResponseJSON({'interactions': [interaction.get_list_object() for interaction in interactions]})
