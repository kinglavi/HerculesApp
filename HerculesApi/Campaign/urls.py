from django.conf.urls import url

from HerculesApi.Campaign.view import CampaignView, get_products_by_campaign_view, get_campaigns_by_user_view, \
    get_campaigns_by_store_view, get_campaigns_by_company_view
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'campaigns', CampaignView)

urlpatterns = [
    url(r'campaigns/(?P<camp_id>[-\d]+)/products/$', get_products_by_campaign_view),
    url(r'campaigns/me/$', get_campaigns_by_user_view),
    url(r'campaigns/byStore/(?P<store_id>[-\d]+)/$', get_campaigns_by_store_view,),
    url(r'campaigns/byCompany/(?P<company_id>[-\d]+)/$', get_campaigns_by_company_view)
]

urlpatterns += router.urls
