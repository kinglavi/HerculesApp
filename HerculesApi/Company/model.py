from HerculesApi.Store.model import Store
from django.contrib.auth.models import Group
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.CharField(max_length=500)
    managers = models.OneToOneField(Group, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
