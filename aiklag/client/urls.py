from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClientViewSet

client_create = ClientViewSet.as_view({
    'post': 'create',
})

# TODO need to discuss
# client_get = ClientViewSet.as_view({
#     'get': 'get',
# })

client_get_via_post = ClientViewSet.as_view({
    'post': 'get'
})

client_update = ClientViewSet.as_view({
    'put': 'update',
    'post': 'update',
})

client_destroy = ClientViewSet.as_view({
    'post': 'destroy',
})

urlpatterns = [
    url(r'^create$', client_create),
    url(r'^get/$', client_get_via_post),
    # TODO need to discuss
    # url(r'^get(?P<pk>[0-9]+)/$', client_get),
    # TODO need to discuss
    # url(r'^update(?P<pk>[0-9]+)/$', client_update),
    url(r'^update/$', client_update),
    url(r'^destroy(?P<pk>[0-9]+)/$', client_destroy),
]

urlpatterns = format_suffix_patterns(urlpatterns)
