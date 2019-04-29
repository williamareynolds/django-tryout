from django.test import TestCase, Client
from django.urls import reverse
from helpers import unexpected_status_code_message
from mock_samples import MOCKS
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from ..models import Sample
from ..serializers import SampleSerializer


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
            HTTP_200_OK,
            unexpected_status_code_message(response.status_code)
        )

        all_samples = Sample.objects.all()
        serializer = SampleSerializer(all_samples, many=True)
        self.assertEqual(response.data,
                         serializer.data,
                         'The data returned from the index endpoint did not '
                         'match the inserted mocks.')


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
            HTTP_200_OK,
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
            HTTP_404_NOT_FOUND,
            unexpected_status_code_message(response.status_code,
                                           HTTP_404_NOT_FOUND)
        )
