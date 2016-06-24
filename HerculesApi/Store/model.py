from HerculesApi.Company.model import Company
from django.db import models


class Store(models.Model):
    company = models.ForeignKey(Company)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    phone_number = models.CharField(max_length=30)
