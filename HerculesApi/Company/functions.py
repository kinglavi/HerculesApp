from httplib import BAD_REQUEST
from HerculesApi.Company.conf import MAXIMUM_NUMBER_OF_COMPANIES_FOR_USER
from HerculesApi.Company.model import Company
from rest_framework.exceptions import NotFound, APIException


def get_companies_by_user(user):
    """
    User can see the company only if he is member of one of the managers groups of the company.
    :return: Query set of companies
    """
    # if admin than all else only user's companies.
    if not user.is_superuser:
        return Company.objects.filter(managers=user)
    else:
        Company.objects.all()


def get_company_by_id(company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Exception as e:
        raise NotFound("Could not find campaign.")
    return company


def is_user_able_to_create_company(user):
    if len(get_companies_by_user(user)) >= MAXIMUM_NUMBER_OF_COMPANIES_FOR_USER:
        e = APIException("User %s already has company." % user.username)
        e.status_code = BAD_REQUEST
        raise e
