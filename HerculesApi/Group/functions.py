from httplib import BAD_REQUEST
from django.contrib.auth.models import Group
from django.db import IntegrityError
from rest_framework.exceptions import APIException


def create_group(user, group_name):
    # TODO: maybe add prefix to the group name to distinguish between company group and store group
    # TODO: or maybe create class for each one of them.
    try:
        g = Group(name=group_name)
        g.save()
    except IntegrityError as e:
        e = APIException("There is already a group name %s. Choose different company name." % group_name)
        e.status_code = BAD_REQUEST
        raise e
    user.groups.add(g)
    return g
