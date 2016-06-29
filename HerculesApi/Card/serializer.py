from HerculesApi.Campaign.serializer import CampaignSerializer
from HerculesApi.Card.model import Card
from HerculesApi.Customer.serializer import CustomerSerializer
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    owner = CustomerSerializer(many=False, read_only=True)
    campaign = CampaignSerializer(many=False, read_only=True)

    class Meta:
        model = Card
        fields = ('id', 'created_at', 'punch_counter',
                  'owner', 'campaign')
