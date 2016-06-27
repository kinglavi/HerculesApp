from HerculesApi.Campaign.model import Campaign
from HerculesApi.Product.serializer import ProductSerializer
from HerculesApi.Store.serializer import StoreSerializer
from rest_framework import serializers


class CampaignSerializer(serializers.ModelSerializer):
    # Maybe serializer the store. hyperlink/nested/slug
    store = StoreSerializer(many=True, read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = ('goal', 'created_at', 'end_date',
                  'description', 'gift_discount', 'product',
                  'store')
