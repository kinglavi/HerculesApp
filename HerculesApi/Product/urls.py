from HerculesApi.Product.view import ProductView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductView)

urlpatterns = router.urls
