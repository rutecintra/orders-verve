from django.db import models
from .appmodel import AppModel

class Products(AppModel):
    sku = models.CharField(max_length=255)
    offerid = models.CharField(max_length=255)
    ean = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
    currency = models.CharField(max_length=50)
    brand = models.CharField(max_length=255)

    class Meta:
        db_table = 'products'