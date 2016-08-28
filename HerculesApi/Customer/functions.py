from HerculesApi.Customer.model import Customer
from rest_framework.exceptions import APIException


def get_customer_store_gifts(cust, store):
    """
    Get all gifts by customer and store.
    :param cust:
    :param store:
    :return:
    """
    pass


def get_customer_gifts(user):
    try:
        customer = Customer.objects.get(username=user.username)
    except Exception as e:
        raise APIException("Could not find user.")

    return customer.gifts.values()
