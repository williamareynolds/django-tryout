from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from trachoma_pgp3_antigen.models import Sample
from trachoma_pgp3_antigen.serializers import SampleSerializer
from ..helpers import unexpected_status_code_message
from ..mock_samples import MOCKS
import json


client = Client()


class IndexSampleTest(TestCase):
    """Tests indexing Sample records from the API"""
    def setUp(self):
        for mock in MOCKS.values():
            Sample.objects.create(**mock)

    def test_index_sample(self):
        response = client.get(
            reverse('api_v1:trachoma_pgp3_antigen:index_create_sample')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            unexpected_status_code_message(response.status_code)
        )

        all_samples = Sample.objects.all()
        serializer = SampleSerializer(all_samples, many=True)
        self.assertEqual(response.data,
                         serializer.data,
                         'The data returned from the index endpoint did not '
                         'match the inserted mocks.')


class SampleCreateTest(TestCase):
    """Test the Sample create endpoint"""
    def setUp(self):
        self.valid_sample = MOCKS['positive']
        self.invalid_sample = MOCKS['negative']
        self.invalid_sample['age_f'] = '{0,-5090]'
        self.url_name = 'api_v1:trachoma_pgp3_antigen:index_create_sample'

    def test_create_valid_sample(self):
        response = client.post(
            reverse(self.url_name),
            json.dumps(self.valid_sample),
            content_type='application/json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            unexpected_status_code_message(response.status_code,
                                           status.HTTP_201_CREATED)
        )

    def test_create_invalid_sample(self):
        response = client.post(
            reverse(self.url_name),
            json.dumps(self.invalid_sample),
            content_type='application/json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            unexpected_status_code_message(response.status_code,
                                           status.HTTP_400_BAD_REQUEST)
        )
