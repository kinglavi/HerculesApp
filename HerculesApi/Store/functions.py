from django.db.models import Q
from rest_framework.exceptions import PermissionDenied, NotFound

from HerculesApi.Company.functions import get_companies_by_user
from HerculesApi.Customer.functions import get_customer_store_gifts
from HerculesApi.Customer.model import Customer
from HerculesApi.Store.model import Store


def get_store_by_id(store_id):
    try:
        store = Store.objects.get(id=store_id)
    except Exception as e:
        raise NotFound("Could not find store.")
    return store


def get_gifts_by_store(user, store_id):
    store = get_store_by_id(store_id)

    if store.managers in user.groups.all() or user.is_superuser:
        gifts = {}
        for customer in Customer.objects.all():
            gifts[customer.username] = get_customer_store_gifts(customer, store)
        return gifts
    else:
        raise PermissionDenied("User %s does not have access." % user)


def get_stores_by_user(user):
    """
    Get all the stores that the user in manager of their company or worker in the store.
    :return Queryset of stores.
    """
    if user.is_superuser:
        qs_stores = Store.objects.all()
    else:
        qs_stores = \
            Store.objects.filter(
                # TODO: Maybe remove managers__in cuz worker cannot edit the store
                Q(managers__in=user.groups.all()) |
                Q(company__in=get_companies_by_user(user)))

    return qs_stores


def get_stores_by_company(company):
    return Store.objects.filter(company=company)
