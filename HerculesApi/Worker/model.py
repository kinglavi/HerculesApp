from django.contrib.auth.models import User
from django.db import models

from HerculesApi.Store.model import Store


class Worker(User):
    store = models.ForeignKey(Store)
    is_manager = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
