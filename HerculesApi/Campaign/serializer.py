from HerculesApi.Campaign.model import Campaign
from HerculesApi.Product.model import Product
from HerculesApi.Product.serializer import ProductSerializer
from HerculesApi.Store.serializer import StoreSerializer
from rest_framework import serializers


class CampaignSerializer(serializers.ModelSerializer):
    # Maybe serializer the store. hyperlink/nested/slug
    # store = StoreSerializer(many=False, read_only=True)
    # products = ProductSerializer(many=True)

    # def create(self, validated_data):
    #     [Product.objects.create(**p) for p in validated_data.pop('products')]
    #     return Campaign.objects.create(**validated_data)

    class Meta:
        model = Campaign
        fields = ('id', 'goal', 'created_at', 'end_date',
                  'description', 'gift_discount', 'store', 'products')
