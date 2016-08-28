from HerculesApi.Customer.functions import get_customer_store_gifts
from HerculesApi.Customer.model import Customer
from HerculesApi.Store.model import Store


def get_gifts_by_store(user, store_id):
    # TODO: user get instead of filter.first
    store = Store.objects.all().filter(id=store_id).first()

    # if user.is_superuser:
    #     pass
    # else:
    #     # TODO: check if user is store manager
    #     gifts= []
    #     for cust in Customer.objects.all():
    #         gifts += get_cust_store_gifts(cust, store)
    #     return gifts.values

    gifts = []
    for cust in Customer.objects.all():
        gifts += get_customer_store_gifts(cust, store)
    return gifts
