from HerculesApi.Product.model import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'description',
                  'sticker_counter', 'price')
