from HerculesApi.Campaign.functions import get_campaign_by_id
from HerculesApi.Company.functions import get_company_by_id
from HerculesApi.Product.functions import get_product_by_id
from HerculesApi.Store.functions import get_store_by_id
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated():
            if request.method in SAFE_METHODS:
                return True
            else:
                return request.user.is_staff or request.user.is_superuser


class IsSuperUserOrIsStaff(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff or request.user.is_superuser


def is_admin_or_company_manager(user, store_id=None, campaign_id=None, company_id=None,
                                include_workers=False, product_id=None):
    """
    Campaign manager means that the user is one of the
    managers of the company (not the store)
    Notice: write now there is no use for the include workers
    :param user:
    :param store_id:
    """
    store = None
    workers = []

    if company_id:
        company = get_company_by_id(company_id)
    else:
        if store_id:
            store = get_store_by_id(store_id)
        elif campaign_id:
            store = get_campaign_by_id(campaign_id).store
        elif product_id:
            store = get_product_by_id(product_id).store
        company = store.company
    managers = company.managers.all()  # list of users
    if store and include_workers:
        workers = store.managers.all()

    return user in managers or user.is_superuser or \
           any(g in user.groups.all() for g in workers)
