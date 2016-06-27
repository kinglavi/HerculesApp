from HerculesApi.Campaign.model import Campaign
from HerculesApi.Product.serializer import ProductSerializer
from rest_framework import serializers


class CampaignSerializer(serializers.ModelSerializer):
    # Maybe serializer the store. hyperlink/nested/slug
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = ('goal', 'created_at', 'end_date',
                  'description', 'gift_discount', 'product')
