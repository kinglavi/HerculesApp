from rest_framework import serializers
from HerculesApi.Card.model import Card


class CardSerializer(serializers.ModelSerializer):
    # owner = CustomerSerializer(many=False, read_only=True)
    # campaign = CampaignSerializer(many=False, read_only=True)

    class Meta:
        model = Card
        fields = ('id', 'created_at', 'punch_counter',
                  'owner', 'campaign')
