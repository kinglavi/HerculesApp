from rest_framework import routers

from HerculesApi.Customer.view import CustomerView

router = routers.SimpleRouter()
router.register(r'customers', CustomerView)

urlpatterns = router.urls
