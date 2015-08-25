import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import ValuesQuerySet
from django.http import HttpResponse


def convert(input_object):
    if isinstance(input_object, ValuesQuerySet):
        return convert(list(input_object))
    elif isinstance(input_object, dict):
        return {convert(key): convert(value) for key, value in input_object.iteritems()}
    elif isinstance(input_object, list):
        return [convert(element) for element in input_object]
    elif isinstance(input_object, unicode):
        return input_object.encode('utf-8')
    else:
        return input_object


class HttpResponseJSON(HttpResponse):

    def __init__(self, content=None):
        content = convert(content) or {}
        if not (isinstance(content, basestring)):
            content = json.dumps(content, cls=DjangoJSONEncoder)
        super(HttpResponseJSON, self).__init__(content=content, content_type='application/simplejson')
