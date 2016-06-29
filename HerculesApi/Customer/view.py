from rest_framework import viewsets

from HerculesApi.Customer.model import Customer
from HerculesApi.Customer.serializer import CustomerSerializer


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
