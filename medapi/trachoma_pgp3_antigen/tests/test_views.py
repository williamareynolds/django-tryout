from django.test import TestCase, Client
from django.urls import reverse
from mock_samples import MOCKS
from rest_framework.status import HTTP_200_OK
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
        self.assertEqual(response.status_code,
                         HTTP_200_OK,
                         'The response from the endpoint was '
                         + str(response.status_code) + ' but should have been '
                         + str(HTTP_200_OK))

        all_samples = Sample.objects.all()
        serializer = SampleSerializer(all_samples, many=True)
        self.assertEqual(response.data,
                         serializer.data,
                         'The data returned from the index endpoint did not '
                         'match the inserted mocks.')
