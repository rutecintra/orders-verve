from django.db import models
from .appmodel import AppModel
from .products import Products

class ProductImages(AppModel):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    image1 = models.CharField(max_length=255, null=True, blank=True)
    image2 = models.CharField(max_length=255, null=True, blank=True)
    image3 = models.CharField(max_length=255, null=True, blank=True)
    image4 = models.CharField(max_length=255, null=True, blank=True)
    image5 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'productimages'