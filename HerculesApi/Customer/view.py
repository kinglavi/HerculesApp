from HerculesApi.Customer.functions import get_customer_gifts
from rest_framework import viewsets

from HerculesApi.Customer.model import Customer
from HerculesApi.Customer.serializer import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


@api_view(['GET'])
def get_customer_gifts_view(request):
    try:
        return Response(get_customer_gifts(request.user))
    except APIException as e:
        raise e
    except Exception as e:
        raise APIException(e.message)
