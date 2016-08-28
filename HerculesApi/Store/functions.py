from HerculesApi.Customer.functions import get_customer_store_gifts
from HerculesApi.Customer.model import Customer
from HerculesApi.Store.model import Store
from rest_framework.exceptions import PermissionDenied, NotFound


def get_gifts_by_store(user, store_id):
    try:
        store = Store.objects.get(id=store_id)
    except Exception as e:
        raise NotFound("Could not find store.")

    if store.managers in user.groups.all() or user.is_superuser:
        gifts = {}
        for customer in Customer.objects.all():
            gifts[customer.username] = get_customer_store_gifts(customer, store)
        return gifts
    else:
        raise PermissionDenied("User %s does not have access." % user)
