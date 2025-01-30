from django.db import models
from src.models.appmodel import AppModel
from src.marketplaces.models import Marketplaces

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

class ProductImages(AppModel):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    image1 = models.CharField(max_length=255, null=True, blank=True)
    image2 = models.CharField(max_length=255, null=True, blank=True)
    image3 = models.CharField(max_length=255, null=True, blank=True)
    image4 = models.CharField(max_length=255, null=True, blank=True)
    image5 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'productimages'

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