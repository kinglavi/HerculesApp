from HerculesApi.Store.functions import get_store_by_id
from HerculesApi.Store.model import Store
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound

from HerculesApi.Campaign.model import Campaign
from HerculesApi.Product.model import Product


def get_products_by_campaign(camp_id):
    """
    :param camp_id: Id of the campaign.
    :return: Queryset of products
    """
    try:
        Campaign.objects.get(id=camp_id)
    except ObjectDoesNotExist as e:
        raise NotFound("Campaign id %s doesnt exists." % camp_id)
    return Product.objects.filter(id=camp_id)


def get_campaign_by_id(campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
    except Exception as e:
        raise NotFound("Could not find campaign.")
    return campaign


def is_admin_or_company_manager(user, store_id=None, campaign_id=None):
    """
    Campaign manager means that the user is one of the
    managers of the company (not the store)
    :param user:
    :param store_id:
    """
    if not store_id:
        store_id = get_campaign_by_id(campaign_id).store.id
    return get_store_by_id(store_id).company.managers in user.groups.all() or user.is_superuser
