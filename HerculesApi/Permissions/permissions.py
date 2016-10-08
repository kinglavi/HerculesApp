from HerculesApi.Campaign.functions import get_campaign_by_id
from HerculesApi.Company.functions import get_company_by_id
from HerculesApi.Store.functions import get_store_by_id
from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated():
            if request.method in SAFE_METHODS:
                return True
            else:
                return request.user.is_staff or request.user.is_superuser


def is_admin_or_company_manager(user, store_id=None, campaign_id=None, company_id=None,
                                managers_group_id=None):
    """
    Campaign manager means that the user is one of the
    managers of the company (not the store)
    :param user:
    :param store_id:
    """
    if managers_group_id:
        managers = Group.objects.get(managers_group_id)
    else:
        if company_id:
            company = get_company_by_id(company_id)
        else:
            if not store_id:
                store_id = get_campaign_by_id(campaign_id).store.id
            company = get_store_by_id(store_id).company
        managers = company.managers

    return managers in user.groups.all() or user.is_superuser
