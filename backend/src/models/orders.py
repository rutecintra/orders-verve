from django.db import models
from .appmodel import AppModel

class Orders(AppModel):
    status_id = models.ForeignKey('orderstatus', on_delete=models.CASCADE)
    marketplacestatus = models.CharField(max_length=100, null=True, blank=True)
    integrationstatus = models.CharField(max_length=100, null=True, blank=True)
    paymentdate = models.DateTimeField(auto_now_add=False)
    integrationorderid = models.CharField(max_length=100, null=False)
    integration_id = models.ForeignKey('integrations', on_delete=models.CASCADE)
    currency = models.CharField(max_length=100, null=True, blank=True)
    customer_id = models.ForeignKey('customers', on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(null=True, blank=True)
    earliestdelivery_date = models.DateTimeField(null=True, blank=True)
    latestdelivery_date = models.DateTimeField(null=True, blank=True)
    totalprice = models.FloatField(null=False)
    totalcomission = models.FloatField(null=False)

    def __str__(self):
        return self.title