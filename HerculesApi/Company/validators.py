from httplib import BAD_REQUEST

from rest_framework.exceptions import APIException

from HerculesApi.Company.functions import get_companies_by_user


def is_user_able_to_create_company(user):
    if len(get_companies_by_user(user)) >= 1:
        e = APIException("User %s already has company." % user.username)
        e.status_code = BAD_REQUEST
        raise e


def company_name_validator(value):
    pass
