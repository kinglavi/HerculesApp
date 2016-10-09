from HerculesApi.Campaign.functions import get_campaigns_by_store, get_campaigns_by_company
from HerculesApi.Company.functions import get_company_by_id
from HerculesApi.Sticker.model import Sticker
from HerculesApi.Store.functions import get_store_by_id
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from rest_framework.exceptions import NotFound, PermissionDenied

from HerculesApi.Card.model import Card


def get_cards_queryset_by_user(user):
    if user.is_superuser:
        queryset = Card.objects.all()
    else:
        queryset = Card.objects.all().filter(owner=user)

    return queryset


def get_group_of_store(store):
    for g in store.admin.groups:
        # TODO: ??
        pass


def get_all_cards_by_store(store_id):
    store = get_store_by_id(store_id)
    return Card.objects.filter(campaign__in=get_campaigns_by_store(store))


def get_all_cards_by_company(company_id):
    company = get_company_by_id(company_id)
    return Card.objects.filter(campaign__in=get_campaigns_by_company(company))


def get_card_by_user(user, sticker):
    try:
        card = Card.objects.get(owner=user,
                                campaign=sticker.product.campaign)
    except MultipleObjectsReturned:
        raise NotFound("More than one card was found.")
    except ObjectDoesNotExist:
        card = sticker.create_card_from_sticker(user)

    if (not card) or (card.owner.username != user.username):
        raise PermissionDenied("User %s doesn't have permission for this card." %
                               user.username)

    return card


def increase_card_punch_counter(user, token):
    sticker = Sticker.get_sticker_by_token(token)
    card = get_card_by_user(user, sticker)
    card.increase_punch_counter(sticker)
