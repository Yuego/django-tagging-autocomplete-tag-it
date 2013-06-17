#coding: utf-8
from __future__ import unicode_literals, absolute_import

import json

from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from tagging.models import Tag

from .models import tagging_has_namespace

def suggest(request):
    tags = []
    term = request.GET.get('term', None)
    if term is not None:
        qs = Tag.objects.filter(name__istartswith=request.GET['term'])

        if tagging_has_namespace:
            namespace = request.GET.get('ns', None)
            if namespace is not None:
                qs = qs.filter(namespace=namespace)
        try:
            tags = qs.values_list('name', flat=True)
        except MultiValueDictKeyError:
            pass

    return JsonResponse([x.encode('utf-8') for x in tags])


class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with ``application/json`` mimetype.
    """
    def __init__(self, data):
        super(JsonResponse, self).__init__(content=json.dumps(data), mimetype='application/json')
