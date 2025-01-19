from django.db import models
from .appmodel import AppModel
from .products import Products
from .marketplaces import Marketplaces

class ProductPrices(AppModel):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Marketplaces, on_delete=models.CASCADE)
    discount_startdate = models.DateField()
    discount_enddate = models.DateField()
    discount = models.FloatField()
    discountprice = models.FloatField()
    originalprice = models.FloatField()

    class Meta:
        db_table = 'productprices'