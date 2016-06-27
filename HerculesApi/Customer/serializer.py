from HerculesApi.Campaign.serializer import CampaignSerializer
from HerculesApi.Group.serializer import GroupSerializer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    gifts = CampaignSerializer(many=True, read_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        fields = ('username', 'gifts', 'email', 'groups')
