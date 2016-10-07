from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from HerculesApi.Company.functions import get_companies_by_user
from HerculesApi.Company.model import Company
from HerculesApi.Company.serializer import CompanySerializer
from HerculesApi.Company.validators import is_user_able_to_create_company


class CompaniesView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return get_companies_by_user(self.request.user)

    def pre_save(self):
        is_user_able_to_create_company(self.request.user)
