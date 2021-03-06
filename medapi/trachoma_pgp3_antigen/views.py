# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Sample
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import SampleSerializer


@api_view(['GET', 'POST'])
def index_create_sample(request):
    if request.method == 'GET':
        serializer = SampleSerializer(Sample.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def read_update_delete_sample(request, id):
    try:
        sample = Sample.objects.get(id=id)
    except Sample.DoesNotExist:
        # DoesNotExist shouldn't hinder execution
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SampleSerializer(sample)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SampleSerializer(sample, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sample.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
