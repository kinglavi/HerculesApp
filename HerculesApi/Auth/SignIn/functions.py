from HerculesApi.Auth.SignIn.conf import CUSTOMER_DEFAULT_FIELDS, FB_GRAPH_API_VERSION, FB_GRAPH_API_URL
from HerculesApi.Customer.model import Customer
from django.contrib.auth import login
from requests import get
from rest_framework.exceptions import APIException


def get_fb_details(fb_token, fields=CUSTOMER_DEFAULT_FIELDS,
                   graph_version=FB_GRAPH_API_VERSION):
    url = FB_GRAPH_API_URL + 'v' + graph_version + '/me?access_token=' + \
          fb_token + '&fields=' + fields.pop()
    for f in fields:
        url += ',' + f

    response = get(url)
    if response.status_code != 200:
        raise APIException("Error occured with facebook graph api. details: %s" %
                           response.content)
    return response.json()


def create_customer(request):
    user_details = request.data
    if 'fb_token' in user_details:
        user_details = get_fb_details(user_details['fb_token'])

    # TODO: check if all data exists.

    new_customer = Customer.objects.create(**user_details)

    login(request, new_customer)
