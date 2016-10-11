from HerculesApi.Company.validators import company_name_validator
from django.contrib.auth.models import Group
from django.core.validators import RegexValidator
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
                            # validators=
                            # [RegexValidator(
                            #     regex='^[a-zA-Z0-9 _-]*$',
                            #     message="Name must be Alphanumberic. (optional characters: _,-, )",
                            #     code="Invalid company name.")])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.CharField(max_length=500)
    managers = models.OneToOneField(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
