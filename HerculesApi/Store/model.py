from HerculesApi.Company.model import Company
from django.contrib.auth.models import Group
from django.db import models

from HerculesApi.Validators.validators import GLOBAL_ALPHANUMERIC_NAME_VALIDATOR


class Store(models.Model):
    name = models.CharField(max_length=200,
                            validators=[GLOBAL_ALPHANUMERIC_NAME_VALIDATOR])
    company = models.ForeignKey(Company)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    phone_number = models.CharField(max_length=30)
    managers = models.ManyToManyField(Group, default=None)

    def __str__(self):
        return self.name
