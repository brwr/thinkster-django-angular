from django.views.decorators.http import require_GET

from utils.http_response import HttpResponseJSON

from models import Interaction, MetaData


@require_GET
def interaction_fields(_):
    interaction_field_names = [field.name for field in Interaction._meta.concrete_fields]
    meta_field_names = [field.name for field in MetaData._meta.concrete_fields]

    return HttpResponseJSON({
        'fields': {
            'interaction': interaction_field_names,
            'meta': meta_field_names,
        },
    })
