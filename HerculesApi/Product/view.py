from HerculesApi.Product.model import Product
from HerculesApi.Product.serializer import ProductSerializer
from rest_framework import viewsets


class ProductView(viewsets.ModelViewSet):
    """
        This is product view set.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
