from django.conf.urls import url
from rest_framework import routers

from HerculesApi.Store.view import StoreView, store_gifts_view

router = routers.SimpleRouter()
router.register(r'stores', StoreView)

urlpatterns = [
    url(r'store-gifts/(?P<store_id>[^/]+)/$', store_gifts_view),
]

urlpatterns += router.urls
