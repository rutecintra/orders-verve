from django.db import models
from .appmodel import AppModel
from .logistics import Logistics

# order shipping packages

class OrderShippings(AppModel):
    shippingprice = models.FloatField()
    estimateddate = models.DateField()
    deliverydate = models.DateField()
    logistic_id = models.ForeignKey(Logistics, on_delete=models.CASCADE)
    tracking = models.CharField(max_length=255)
    tracking_url = models.CharField(max_length=255)
    zonecode = models.CharField(max_length=50)

    class Meta:
        db_table = 'ordershippings'