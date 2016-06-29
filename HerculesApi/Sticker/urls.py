from rest_framework import routers

from HerculesApi.Sticker.view import StickersView

router = routers.SimpleRouter()
router.register(r'stickers', StickersView)

urlpatterns = router.urls
