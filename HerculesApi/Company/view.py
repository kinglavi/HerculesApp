from HerculesApi.Permissions.permissions import is_admin_or_company_manager
from rest_framework import viewsets
from rest_framework.compat import is_authenticated
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework.permissions import IsAuthenticated

from HerculesApi.Company.functions import get_companies_by_user
from HerculesApi.Company.model import Company
from HerculesApi.Company.serializer import CompanySerializer
from HerculesApi.Company.validators import is_user_able_to_create_company
from rest_framework.response import Response


class CompaniesView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, managers_group_id=request.data['managers']):
            return super(CompaniesView, self).create(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can create campaigns.")

    def update(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, managers_group_id=request.data['managers']):
            return super(CompaniesView, self).update(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can edit campaigns.")

    def destroy(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, company_id=kwargs.get('pk')):
            return super(CompaniesView, self).destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can edit campaigns.")

    def perform_create(self, serializer):
        is_user_able_to_create_company(self.request.user)


@api_view(['GET'])
def get_companies_by_user_view(request):
    """
    Get only the companies that the user has permission to edit.
    :param request:
    :return:
    """
    if is_authenticated(request.user):
        return Response(get_companies_by_user(request.user).values())
    else:
        raise NotAuthenticated
