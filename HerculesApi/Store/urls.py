from rest_framework import routers

from HerculesApi.Store.view import StoreView

router = routers.SimpleRouter()
router.register(r'stores', StoreView)

urlpatterns = router.urls
