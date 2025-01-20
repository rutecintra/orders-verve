from django.db import models
from .appmodel import AppModel
from .orders import Orders

class Invoices(AppModel):
    accesskey = models.CharField(max_length=255)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)

    class Meta:
        db_table = 'invoices'