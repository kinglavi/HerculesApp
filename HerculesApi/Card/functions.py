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


def get_card_by_user(user, card_id):
    # TODO: user get instead of filter.first
    card = Card.objects.all().filter(id=card_id).first()

    if not card:
        raise NotFound("Could not find card %s" % card_id)
    # Check permission of the user
    elif card.owner == user:
        return card
    else:
        raise PermissionDenied("User %s doesn't have permission for card %s." % (user.username, card_id))


def increase_card_punch_counter(user, card_id, token):

    card = get_card_by_user(user, card_id)
    # TODO: if card doesnt exists - create new one.
    card.increase_punch_counter(token)
