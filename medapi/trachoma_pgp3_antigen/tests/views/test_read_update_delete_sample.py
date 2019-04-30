from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from trachoma_pgp3_antigen.models import Sample
from trachoma_pgp3_antigen.serializers import SampleSerializer
from ..helpers import unexpected_status_code_message
from ..mock_samples import MOCKS


client = Client()


class ReadSampleTest(TestCase):
    """Tests getting a sample which exists, and one which does not"""
    def setUp(self):
        self.sample = Sample.objects.create(**MOCKS.values()[0])
        self.url_name = 'api_v1:trachoma_pgp3_antigen:read_update_delete_sample'

    def test_read_existing_sample(self):
        response = client.get(
            reverse(self.url_name, kwargs={'id': self.sample.id})
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
            reverse(self.url_name, kwargs={'id': 99999})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
            unexpected_status_code_message(response.status_code,
                                           status.HTTP_404_NOT_FOUND)
        )
