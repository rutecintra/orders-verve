from django.db import models
from models.appmodel import RelationshipModel
from orders.models import Orders
from orders.models import OrderShippings
from orders.models import OrderProducts
from products.models import Products
from categories.models import Categories
from logistics.models import Logistics

class OrdersOrderShippings(RelationshipModel):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ordershippings = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders_ordershippings'

class OrderProductsOrderShippings(RelationshipModel):
    orderproducts = models.ForeignKey(OrderProducts, on_delete=models.CASCADE)
    ordershippings = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)
    receiveddate  = models.DateField(null=True, blank=True)
    shipped_date  = models.DateField(null=True, blank=True)

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