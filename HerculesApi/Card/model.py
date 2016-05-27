from django.db import models

from HerculesApi.Customer.model import Customer
from HerculesApi.Store.model import Store


class Card(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
