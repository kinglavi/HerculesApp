from HerculesApi.Campaign.model import Campaign
from django.contrib.auth.models import User
from django.db import models


class Customer(User):
    gifts = models.ManyToManyField(Campaign, null=True)
