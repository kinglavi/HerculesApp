from rest_framework.exceptions import NotFound

from HerculesApi.Card.model import Card
from HerculesApi.Customer.model import Customer
from HerculesApi.Product.model import Product
from django.db import models

# TODO: dont import all
from datetime import datetime


class Sticker(models.Model):
    token = models.CharField(max_length=500)
    is_used = models.BooleanField(default=False)
    product = models.ForeignKey(Product)

    # qr_picture_url = models.CharField(max_length=500, default=None)
    #
    # def create_url_from_hash(self):
    #     """
    #     Create QR url with the self.hash parameter.
    #     :return:
    #     """
    #     return self.hash

    def create_card_from_sticker(self, user):
        # TODO: don't get customer from card module
        c = Card(created_at=datetime.now(), campaign=self.product.campaign,
                 owner=Customer.objects.get(username=user))
        c.save()
        return c

    @staticmethod
    def get_sticker_by_token(token):
        try:
            sticker = Sticker.objects.get(token=token)
        except Exception as e:
            # Sticker was not found or more than one sticker has the same token.
            return NotFound("Could not find sticker.")

        return sticker
