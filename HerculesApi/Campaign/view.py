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