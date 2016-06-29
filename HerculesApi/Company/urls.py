from rest_framework import routers

from HerculesApi.Company.view import CompaniesView

router = routers.SimpleRouter()
router.register(r'companies', CompaniesView)

urlpatterns = router.urls
