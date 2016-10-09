from HerculesApi.Product.serializer import ProductSerializer
from HerculesApi.Sticker.model import Sticker
from rest_framework import serializers


class StickerSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = Sticker
        fields = ('id', 'token', 'is_used', 'product')
