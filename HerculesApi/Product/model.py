from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    # secret_key = models.CharField(max_length=100)
    sticker_counter = models.IntegerField(default=0)
    price = models.IntegerField()

    def increase_sticker_counter(self):
        self.sticker_counter += 1
        self.save()
