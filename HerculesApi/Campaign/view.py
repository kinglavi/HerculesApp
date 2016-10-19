from HerculesApi.Campaign.validation import validate_campaign_data
from HerculesApi.Permissions.permissions import is_admin_or_company_manager, is_able_to_modify_campaign
from HerculesApi.Product.functions import has_store_permission_on_products
from rest_framework.compat import is_authenticated
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from HerculesApi.Campaign.functions import get_products_by_campaign, get_campaigns_by_user, get_campaigns_by_store, \
    get_campaigns_by_company
from HerculesApi.Campaign.model import Campaign
from HerculesApi.Campaign.serializer import CampaignSerializer
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK


class CampaignView(viewsets.ModelViewSet):
    """
        This is Campaign view set.
    """
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()

    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        is_able_to_modify_campaign(request.user,
                                   request.data['store'],
                                   request.data.pop('products'))
        return super(CampaignView, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        is_able_to_modify_campaign(request.user,
                                   request.data['store'],
                                   request.data['products'])
        return super(CampaignView, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, campaign_id=kwargs.get('pk')):
            return super(CampaignView, self).destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can edit campaigns.")

    def perform_create(self, serializer):
        validate_campaign_data(self.request.data)
        super(CampaignView, self).perform_create(serializer)


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
    if not is_authenticated(request.user):
        raise PermissionDenied("You must be logged in to see this page..")
    return Response(get_products_by_campaign(camp_id).values())


@api_view(['GET'])
def get_campaigns_by_store_view(request, store_id):
    if not is_authenticated(request.user):
        raise PermissionDenied("You must be logged in to see this page..")
    return Response(get_campaigns_by_store(store_id).values(), status=HTTP_200_OK)


@api_view(['GET'])
def get_campaigns_by_company_view(request, company_id):
    if not is_authenticated(request.user):
        raise PermissionDenied("You must be logged in to see this page..")
    return Response(get_campaigns_by_company(company_id).values(), status=HTTP_200_OK)
