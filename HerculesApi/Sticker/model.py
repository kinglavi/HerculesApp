from HerculesApi.Product.model import Product
from django.db import models


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
