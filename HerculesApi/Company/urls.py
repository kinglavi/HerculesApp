from django.conf.urls import url
from rest_framework import routers

from HerculesApi.Company.view import CompaniesView, get_companies_by_user_view

router = routers.SimpleRouter()
router.register(r'companies', CompaniesView)

urlpatterns = [
    url(r'companies/me/$', get_companies_by_user_view)
]

urlpatterns += router.urls
