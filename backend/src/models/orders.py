from django.db import models
from .appmodel import AppModel
from .orderstatus import Orderstatus
from .integrations import Integrations
from .customers import Customers

class Orders(AppModel):
    status_id = models.ForeignKey(Orderstatus, on_delete=models.CASCADE)
    marketplacestatus = models.CharField(max_length=100, null=True, blank=True)
    integrationstatus = models.CharField(max_length=100, null=True, blank=True)
    paymentdate = models.DateTimeField(auto_now_add=False)
    integrationorderid = models.CharField(max_length=100, null=False)
    integration_id = models.ForeignKey(Integrations, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100, null=True, blank=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(null=True, blank=True)
    earliestdelivery_date = models.DateTimeField(null=True, blank=True)
    latestdelivery_date = models.DateTimeField(null=True, blank=True)
    totalprice = models.FloatField(null=False)
    totalcomission = models.FloatField(null=False)

    class Meta:
        db_table = 'orders'