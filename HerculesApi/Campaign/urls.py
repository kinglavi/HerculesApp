from HerculesApi.Campaign.view import CampaignView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'campaigns', CampaignView)

urlpatterns = router.urls
