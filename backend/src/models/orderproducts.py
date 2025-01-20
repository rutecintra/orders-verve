from django.db import models
from .appmodel import AppModel
from .products import Products
from .orders import Orders
from .ordershippings import OrderShippings

# products will be created per order, so the same SKU may be repeated

class OrderProducts(AppModel):
    sku = models.CharField(max_length=255)
    commission_fee = models.FloatField()
    price = models.FloatField()
    quantity = models.IntegerField()
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    shippings = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orderproducts'