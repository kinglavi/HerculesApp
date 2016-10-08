from HerculesApi.Product.model import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'store')
