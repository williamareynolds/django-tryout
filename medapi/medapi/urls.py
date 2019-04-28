"""medapi URL Configuration

Because medapi provides a versioned rest api, we can helpfully utilize url
namespacing to separate versions and applications during reverse url resolution.
"""
from django.conf.urls import include, url


api_v1 = [
    url(r'^trachoma_pgp3_antigen/',
        include(
            'trachoma_pgp3_antigen.urls',
            namespace='trachoma_pgp3_antigen'))
]

urlpatterns = [
    url(r'^api/v1/', include(api_v1, namespace='api_v1'))
]
