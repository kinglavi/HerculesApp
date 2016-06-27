from HerculesApi.Product.serializer import ProductSerializer
from rest_framework import serializers


class StickerSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        fields = ('token', 'is_used', 'product')
