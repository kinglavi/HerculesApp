from rest_framework import viewsets

from HerculesApi.Company.model import Company
from HerculesApi.Company.serializer import CompanySerializer


class CompaniesView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
