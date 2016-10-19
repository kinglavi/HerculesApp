from HerculesApi.Company.validators import company_name_validator
from django.contrib.auth.models import User

from django.core.validators import RegexValidator
from django.db import models

from HerculesApi.Validators.validators import GLOBAL_ALPHANUMERIC_NAME_VALIDATOR


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            validators=
                            [GLOBAL_ALPHANUMERIC_NAME_VALIDATOR])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.CharField(max_length=500)
    managers = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
