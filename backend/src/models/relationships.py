from django.db import models
from .appmodel import RelationshipModel
from .orders import Orders
from .ordershippings import OrderShippings
from .orderproducts import OrderProducts
from .products import Products
from .categories import Categories
from .logistics import Logistics

class OrdersOrderShippings(RelationshipModel):
    _out = models.ForeignKey(Orders, on_delete=models.CASCADE)
    _in = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders_ordershippings'

class OrderProductsOrderShippings(RelationshipModel):
    _out = models.ForeignKey(OrderProducts, on_delete=models.CASCADE)
    _in = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orderproducts_ordershippings'

class ProductsCategories(RelationshipModel):
    _out = models.ForeignKey(Products, on_delete=models.CASCADE)
    _in = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_categories'

class ProductsLogistics(RelationshipModel):
    _out = models.ForeignKey(Products, on_delete=models.CASCADE)
    _in = models.ForeignKey(Logistics, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_logistics'