from HerculesApi.Campaign.serializer import CampaignSerializer
from HerculesApi.Customer.serializer import CustomerSerializer
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    owner = CustomerSerializer(many=False, read_only=True)
    campaign = CampaignSerializer(many=False, read_only=True)

    class Meta:
        fields = ('id', 'created_at', 'punch_counter',
                  'owner', 'campaign')
