from django.conf.urls import url
from rest_framework import routers
from HerculesApi.Card.view import CardsView, increase_card_counter_view, get_all_cards_by_store_view, \
    get_all_cards_by_company_view

router = routers.SimpleRouter()
router.register(r'cards', CardsView)

urlpatterns = [
    url(r'cards/inc/$', increase_card_counter_view),
    url(r'cards/byStore/(?P<store_id>[-\d]+)/$', get_all_cards_by_store_view,),
    url(r'cards/byCompany/(?P<company_id>[-\d]+)/$', get_all_cards_by_company_view)
]

urlpatterns += router.urls
