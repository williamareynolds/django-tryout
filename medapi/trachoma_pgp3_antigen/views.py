# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Sample
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import SampleSerializer


@api_view(['GET', 'POST'])
def index_create_sample(request):
    if request.method == 'GET':
        serializer = SampleSerializer(Sample.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response({})


@api_view(['GET', 'PUT', 'DELETE'])
def read_update_delete_sample(request, id):
    return Response({})
