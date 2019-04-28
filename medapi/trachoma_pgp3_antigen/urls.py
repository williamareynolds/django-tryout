from django.conf.urls import url
import views


urlpatterns = [
    url(r'^samples/$',
        views.index_create_sample,
        name='index_create_sample'),
    url(r'^samples/(?P<id>\d+)/$',
        views.read_update_delete_sample,
        name='read_update_delete_sample'),
]