from django.db import models
from .appmodel import RelationshipModel

class OrdersOrderShippings(RelationshipModel):
    _out = models.ForeignKey('orders.Orders', on_delete=models.CASCADE)
    _in = models.ForeignKey('ordershippings.OrderShippings', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders_ordershippings'

class OrderProductsOrderShippings(RelationshipModel):
    _out = models.ForeignKey('orderproducts.OrderProducts', on_delete=models.CASCADE)
    _in = models.ForeignKey('ordershippings.OrderShippings', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ordersproducts_ordershippings'

class ProductsCategories(RelationshipModel):
    _out = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    _in = models.ForeignKey('categories.Categories', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_categories'

class ProductsLogistics(RelationshipModel):
    _out = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    _in = models.ForeignKey('logistics.Logistics', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_logistics'