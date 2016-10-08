from datetime import datetime, timedelta
from httplib import BAD_REQUEST
from HerculesApi.Campaign.conf import MINIMAL_DAYS_FOR_CAMPAIGN
from rest_framework.exceptions import APIException


def validate_campaign_data(data):
    """
    1. Check that the end date is bigger than the current date by at least one day.
    :param data:
    :return:
    """
    if datetime.now() >= datetime.strptime(data['end_date'],
                                           '%Y-%m-%dT%H:%M') - timedelta(days=MINIMAL_DAYS_FOR_CAMPAIGN):
        e = APIException("Campaign end date must be at least 1 day.")
        e.status_code = BAD_REQUEST
        raise e
