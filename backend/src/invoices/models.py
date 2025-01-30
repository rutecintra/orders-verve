from django.db import models
from src.models.appmodel import AppModel
from src.orders.models import Orders

class Invoices(AppModel):
    accesskey = models.CharField(max_length=255, null=True, blank=True)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)

    class Meta:
        db_table = 'invoices'