from django.conf.urls import url

from HerculesApi.Campaign.view import CampaignView, get_products_by_campaign_view
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'campaigns', CampaignView)

urlpatterns = [
    url(r'campaigns/(?P<camp_id>[-\d]+)/products/$', get_products_by_campaign_view)
]

urlpatterns += router.urls
