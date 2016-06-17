from HerculesApi.Campaign.conf import DEFAULT_CAMPAIGN_TIME
from HerculesApi.Product.model import Product
from django.db import models


class Campaign(models.Model):
    product = models.OneToOneField(Product)
    goal = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_date_value = None if DEFAULT_CAMPAIGN_TIME is None\
        else created_at+DEFAULT_CAMPAIGN_TIME
    end_date = models.DateTimeField(editable=False, default=end_date_value)

    description = models.CharField(max_length=500)
    gift_discount = models.IntegerField()
    secret_key = models.CharField(max_length=100)