from django.db import models
from .appmodel import AppModel
from .products import Products
from .marketplaces import Marketplaces

class ProductPrices(AppModel):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    marketplaces = models.ForeignKey(Marketplaces, on_delete=models.CASCADE)
    discount_startdate = models.DateField(null=True, blank=True)
    discount_enddate = models.DateField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    discountprice = models.FloatField(null=True, blank=True)
    originalprice = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'productprices'