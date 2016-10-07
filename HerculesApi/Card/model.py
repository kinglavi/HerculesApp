from rest_framework.exceptions import ValidationError, NotFound, APIException

from HerculesApi.Campaign.model import Campaign
from HerculesApi.Customer.model import Customer
from django.db import models

from HerculesApi.Sticker.model import Sticker


class Card(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
    punch_counter = models.IntegerField(default=0)
    owner = models.ForeignKey(Customer)

    def increase_punch_counter(self, sticker):
        if self.punch_counter > self.campaign.goal:
            raise APIException("Counter cannot be bigger than the goal")
        elif sticker.is_used:
            raise ValidationError("Sticker is already used.")

        sticker.is_used = True
        self.punch_counter += 1

        if self.punch_counter == self.campaign.goal:
            self.owner.gifts.add(self.campaign)
            # TODO: transaction
            self.delete()
            sticker.save()
            return

        # TODO: create a transaction that save both sticker and card together
        sticker.save()
        self.save()


