from django.db import models
from .appmodel import AppModel
from .logistics import Logistics

# order shipping packages

class OrderShippings(AppModel):
    shippingprice = models.FloatField(null=True, blank=True)
    estimateddate = models.DateField(null=True, blank=True)
    logistics = models.ForeignKey(Logistics, on_delete=models.CASCADE)
    tracking = models.CharField(max_length=255, null=True, blank=True)
    tracking_url = models.CharField(max_length=255, null=True, blank=True)
    zonecode = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'ordershippings'