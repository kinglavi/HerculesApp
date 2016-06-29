from rest_framework import routers

from HerculesApi.Card.view import CardsView

router = routers.SimpleRouter()
router.register(r'cards', CardsView)

urlpatterns = router.urls
