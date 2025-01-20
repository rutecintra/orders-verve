from django.db import models
from .appmodel import AppModel
from .products import Products
from .orders import Orders
from .ordershippings import OrderShippings

# products will be created per order, so the same SKU may be repeated

class OrderProducts(AppModel):
    sku = models.CharField(max_length=255, null=True, blank=True)
    commission_fee = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    shippings = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)
    image1 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'orderproducts'