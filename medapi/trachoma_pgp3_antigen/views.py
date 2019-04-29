# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Sample
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
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
    try:
        sample = Sample.objects.get(id=id)
    except Sample.DoesNotExist:
        # DoesNotExist shouldn't hinder execution
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SampleSerializer(sample)
        return Response(serializer.data)

    elif request.method == 'PUT':
        return Response({})

    elif request.method == 'DELETE':
        return Response({})
