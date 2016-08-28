from django.conf.urls import url
from rest_framework import routers

from HerculesApi.Customer.view import CustomerView, get_customer_gifts_view

router = routers.SimpleRouter()
router.register(r'customers', CustomerView)

urlpatterns = [
    url(r'^gifts/$', get_customer_gifts_view),
]

urlpatterns += router.urls

