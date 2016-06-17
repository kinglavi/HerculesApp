from HerculesApi.Campaign.model import Campaign
from django.db import models


class Card(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
    auto_counter = models.AutoField()


