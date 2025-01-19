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
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    shipping_id = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orderproducts'