from django.db import models
from .appmodel import RelationshipModel
from .orders import Orders
from .ordershippings import OrderShippings
from .orderproducts import OrderProducts
from .products import Products
from .categories import Categories
from .logistics import Logistics

class OrdersOrderShippings(RelationshipModel):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ordershippings = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders_ordershippings'

class OrderProductsOrderShippings(RelationshipModel):
    orderproducts = models.ForeignKey(OrderProducts, on_delete=models.CASCADE)
    ordershippings = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orderproducts_ordershippings'

class ProductsCategories(RelationshipModel):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_categories'

class ProductsLogistics(RelationshipModel):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    logistics = models.ForeignKey(Logistics, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_logistics'