from HerculesApi.Store.functions import get_stores_by_user, get_stores_by_company
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


def get_campaigns_by_store(store):
    # TODO: maybe check if the store exists.
    return Campaign.objects.filter(store=store)


def get_campaigns_by_company(company):
    return Campaign.objects.filter(store__in=get_stores_by_company(company))


def get_campaigns_by_user(user):
    """
    Get all the campaign that the user in work in their store or his manager of the company.
    """
    return Campaign.objects.filter(store__in=get_stores_by_user(user))


def get_campaign_by_id(campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
    except Exception as e:
        raise NotFound("Could not find campaign.")
    return campaign
