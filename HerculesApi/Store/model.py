from django.db import models

from HerculesApi.Company.model import Company


class Store(models.Model):
    company = models.ForeignKey(Company)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # store_manager =