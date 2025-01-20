from django.db import models
from .appmodel import AppModel

class Products(AppModel):
    sku = models.CharField(max_length=255)
    offerid = models.CharField(max_length=255, null=True, blank=True)
    ean = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    currency = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'products'