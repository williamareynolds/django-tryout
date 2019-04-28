# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def index_create_sample(request):
    return Response({})


@api_view(['GET', 'PUT', 'DELETE'])
def read_update_delete_sample(request, id):
    return Response({})
