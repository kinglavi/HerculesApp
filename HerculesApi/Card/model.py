from HerculesApi.Campaign.model import Campaign
from HerculesApi.Customer.model import Customer
from django.db import models


class Card(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
    punch_counter = models.IntegerField(default=0)
    owner = models.ForeignKey(Customer)

    def increase_punch_counter(self):
        self.auto_counter += 1


