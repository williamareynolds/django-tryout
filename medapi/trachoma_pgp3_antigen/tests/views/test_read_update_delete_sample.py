from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from trachoma_pgp3_antigen.models import Sample
from trachoma_pgp3_antigen.serializers import SampleSerializer
from ..helpers import unexpected_status_code_message
from ..mock_samples import MOCKS
import json


client = Client()
URL_NAME = 'api_v1:trachoma_pgp3_antigen:read_update_delete_sample'


class ReadSampleTest(TestCase):
    """Tests getting a sample which exists, and one which does not"""
    def setUp(self):
        self.sample = Sample.objects.create(**MOCKS['mixed'])

    def test_read_existing_sample(self):
        response = client.get(
            reverse(URL_NAME, kwargs={'id': self.sample.id})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            unexpected_status_code_message(response.status_code)
        )

        serializer = SampleSerializer(self.sample)
        self.assertEqual(response.data, serializer.data)

    def test_read_nonexistent_sample(self):
        response = client.get(
            reverse(URL_NAME, kwargs={'id': 99999})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
            unexpected_status_code_message(response.status_code,
                                           status.HTTP_404_NOT_FOUND)
        )


class UpdateSampleTest(TestCase):
    """Tests updating a sample"""
    def setUp(self):
        self.sample = Sample.objects.create(**MOCKS['negative'])
        self.route = reverse(URL_NAME, kwargs={'id': self.sample.id})
        changed_data = {
            'age': 20,
            'sex': 2,
            'age_f': '[10,20)'
        }
        self.valid_update_data = MOCKS['negative']
        self.valid_update_data.update(changed_data)

    def test_update_existing_sample(self):
        pre_update_sample_count = Sample.objects.count()
        response = client.put(
            self.route,
            json.dumps(self.valid_update_data),
            content_type='application/json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
            unexpected_status_code_message(response.status_code,
                                           status.HTTP_204_NO_CONTENT)
        )
        self.assertEqual(
            Sample.objects.count(),
            pre_update_sample_count,
            'No new records should be created during an update.'
        )

    def test_update_nonexistent_sample(self):
        response = client.put(
            reverse(URL_NAME, kwargs={'id': 99999}),
            json.dumps(self.valid_update_data),
            content_type='application/json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
            unexpected_status_code_message(response.status_code,
                                           status.HTTP_404_NOT_FOUND)
        )

    def test_update_sample_with_invalid_payload(self):
        response = client.put(
            self.route,
            json.dumps({'age': 'b.well'}),
            content_type='application/json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            unexpected_status_code_message(response.status_code,
                                           status.HTTP_400_BAD_REQUEST)
        )
