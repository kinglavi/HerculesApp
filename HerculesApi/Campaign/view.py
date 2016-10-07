from rest_framework.decorators import api_view
from rest_framework.response import Response

from HerculesApi.Campaign.functions import get_products_by_campaign
from HerculesApi.Campaign.model import Campaign
from HerculesApi.Campaign.serializer import CampaignSerializer
from rest_framework import viewsets


class CampaignView(viewsets.ModelViewSet):
    """
        This is Campaign view set.
    """
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()

    # permission_classes = ()

    # TODO: user has to see only his own campaigns.
    # def get_queryset(self):
    #     pass

    def pre_save(self):
        # TODO: check the end_date is bigger than created_at
        print "lavigever"


@api_view(['GET'])
def get_products_by_campaign_view(request, camp_id):
    return Response(get_products_by_campaign(camp_id).values())
