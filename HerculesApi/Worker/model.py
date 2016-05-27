from django.contrib.auth.models import User
from django.db import models

from HerculesApi.Company.model import Company
from HerculesApi.Store.model import Store


class Worker(User):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.ForeignKey(Company)
    store = models.ForeignKey(Store)
    is_manager = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
