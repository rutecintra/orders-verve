from django.db import models
from .appmodel import AppModel

class Customers(AppModel):
    integrationcustomerid = models.CharField(max_length=255, null=True, blank=True)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'customers'