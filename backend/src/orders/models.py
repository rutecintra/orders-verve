from django.db import models
from models.appmodel import AppModel
from products.models import Products
from integrations.models import Integrations
from customers.models import Customers
from logistics.models import Logistics

# products will be created per order, so the same SKU may be repeated

class OrderStatus(AppModel):
    suspend = models.BooleanField(default=False)

    class Meta:
        db_table = 'orderstatus'

class Orders(AppModel):
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, null=True, blank=True)
    marketplacestatus = models.CharField(max_length=100, null=True, blank=True)
    integrationstatus = models.CharField(max_length=100, null=True, blank=True)
    paymentdate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    integrationorderid = models.CharField(max_length=100, null=False)
    integrations = models.ForeignKey(Integrations, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100, null=True, blank=True)
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    earliestdelivery_date = models.DateTimeField(null=True, blank=True)
    latestdelivery_date = models.DateTimeField(null=True, blank=True)
    totalprice = models.FloatField(null=False)
    totalcomission = models.FloatField(null=True)

    class Meta:
        db_table = 'orders'

class OrderShippings(AppModel):
    shippingprice = models.FloatField(null=True, blank=True)
    estimateddate = models.DateField(null=True, blank=True)
    logistics = models.ForeignKey(Logistics, on_delete=models.CASCADE)
    tracking = models.CharField(max_length=255, null=True, blank=True)
    tracking_url = models.CharField(max_length=255, null=True, blank=True)
    zonecode = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'ordershippings'

class OrderProducts(AppModel):
    sku = models.CharField(max_length=255, null=True, blank=True)
    commission_fee = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="orderproducts")
    shippings = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)
    image1 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'orderproducts'