from django.db import models
from .appmodel import AppModel

class Customers(AppModel):
    integrationcustomerid = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    class Meta:
        db_table = 'customers'