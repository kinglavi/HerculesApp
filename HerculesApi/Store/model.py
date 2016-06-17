from HerculesApi.Campaign.model import Campaign
from django.contrib.auth.models import Group
from django.db import models


class Store(models.Model):
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    phone_number = models.CharField(max_length=30)
    campaigns = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    admins = models.ForeignKey(Group)
