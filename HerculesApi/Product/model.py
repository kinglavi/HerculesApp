from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    # secret_key = models.CharField(max_length=100)
    auto_sticker_counter = models.AutoField()
    price = models.IntegerField()
    stickers = models.ForeignKey(Sticker)
