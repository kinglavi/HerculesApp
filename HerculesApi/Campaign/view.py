from HerculesApi.Campaign.model import Campaign
from HerculesApi.Campaign.serializer import CampaignSerializer
from rest_framework import viewsets


class CampaignView(viewsets.ModelViewSet):
    """
        This is Campaign view set.
    """
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()
