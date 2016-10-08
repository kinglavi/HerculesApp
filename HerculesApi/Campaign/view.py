from HerculesApi.Campaign.validation import validate_campaign_data
from HerculesApi.Permissions.permissions import is_admin_or_company_manager
from rest_framework.compat import is_authenticated
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from HerculesApi.Campaign.functions import get_products_by_campaign, get_campaigns_by_user
from HerculesApi.Campaign.model import Campaign
from HerculesApi.Campaign.serializer import CampaignSerializer
from rest_framework import viewsets


class CampaignView(viewsets.ModelViewSet):
    """
        This is Campaign view set.
    """
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()

    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, store_id=request.data['store']):
            return super(CampaignView, self).create(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can create campaigns.")

    def update(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, store_id=request.data['store']):
            return super(CampaignView, self).update(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can edit campaigns.")

    def destroy(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, campaign_id=kwargs.get('pk')):
            return super(CampaignView, self).destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can edit campaigns.")

    def perform_create(self, serializer):
        validate_campaign_data(self.request.data)


@api_view(['GET'])
def get_campaigns_by_user_view(request):
    """
    Get only the campaigns that the user has permission to edit.
    :param request:
    :return:
    """
    if is_authenticated(request.user):
        return Response(get_campaigns_by_user(request.user).values())
    else:
        raise NotAuthenticated


@api_view(['GET'])
def get_products_by_campaign_view(request, camp_id):
    return Response(get_products_by_campaign(camp_id).values())
