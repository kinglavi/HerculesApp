from HerculesApi.Product.model import Product
from HerculesApi.Store.functions import get_stores_by_user
from rest_framework.exceptions import NotFound


def get_product_by_id(product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        raise NotFound("Could not find campaign.")
    return product


def get_products_by_user(user):
    return Product.objects.filter(store__in=get_stores_by_user(user))
