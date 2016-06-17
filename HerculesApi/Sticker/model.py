from django.db import models


class Sticker(models.Model):
    hash = models.CharField(max_length=500)
    qr_picture_url = models.CharField(max_length=500, default=None)

    def create_url_from_hash(self):
        """
        Create QR url with the self.hash parameter.
        :return:
        """
        return self.hash
