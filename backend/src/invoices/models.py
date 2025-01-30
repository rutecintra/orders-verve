from django.db import models
from models.appmodel import AppModel
from orders.models import Orders

class Invoices(AppModel):
    accesskey = models.CharField(max_length=255, null=True, blank=True)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)

    class Meta:
        db_table = 'invoices'