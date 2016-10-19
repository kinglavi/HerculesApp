from HerculesApi.Product.model import Product
from HerculesApi.Store.functions import get_stores_by_user, get_store_by_id
from rest_framework.exceptions import NotFound


def get_product_by_id(product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        raise NotFound("Could not find campaign.")
    return product


def get_products_by_user(user):
    return Product.objects.filter(store__in=get_stores_by_user(user))


def has_store_permission_on_products(store, products):
    """
    Check if the given products are in the store products.
    :param store:
    :param products: list of products ids.
    :return: True/False
    """
    store_products = get_store_by_id(store).product_set.all()
    store_products_ids = [p.id for p in store_products]
    return all(int(p) in store_products_ids for p in products)


