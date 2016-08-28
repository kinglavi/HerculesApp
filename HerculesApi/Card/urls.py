from django.conf.urls import url
from rest_framework import routers
from HerculesApi.Card.view import CardsView, increase_card_counter_view

router = routers.SimpleRouter()
router.register(r'cards', CardsView)

urlpatterns = [
    url(r'cards/(?P<card_id>[^/]+)/inc$', increase_card_counter_view),
]

urlpatterns += router.urls
