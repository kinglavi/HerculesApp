from datetime import timedelta
from HerculesApi.Campaign.conf import DEFAULT_CAMPAIGN_TIME_IN_DAYS
from HerculesApi.Product.model import Product
from HerculesApi.Store.model import Store
from django.db import models


class Campaign(models.Model):
    store = models.ForeignKey(Store)
    goal = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    end_date = models.DateTimeField(default=None)
    end_date_value = None if end_date is not None\
        else created_at+timedelta(days=DEFAULT_CAMPAIGN_TIME_IN_DAYS)

    description = models.CharField(max_length=500)
    gift_discount = models.IntegerField()
    # secret_key = models.CharField(max_length=100)
