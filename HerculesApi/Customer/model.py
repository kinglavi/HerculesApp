from HerculesApi.Campaign.model import Campaign
from HerculesApi.Card.model import Card
from django.contrib.auth.models import User
from django.db import models


class Customer(User):
    cards = models.ForeignKey(Card, on_delete=models.CASCADE)
    gifts = models.ForeignKey(Campaign)
