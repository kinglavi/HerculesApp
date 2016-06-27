from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'stores', StoreView)

urlpatterns = router.urls
