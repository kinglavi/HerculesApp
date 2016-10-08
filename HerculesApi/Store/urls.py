from django.conf.urls import url
from rest_framework import routers

from HerculesApi.Store.view import StoreView, store_gifts_view, get_stores_by_user_view

router = routers.SimpleRouter()
router.register(r'stores', StoreView)

urlpatterns = [
    url(r'^stores/gifts/(?P<store_id>[^/]+)/$', store_gifts_view),
    url(r'stores/me/$', get_stores_by_user_view)
]

urlpatterns += router.urls
