from django.db import models
from .appmodel import AppModel
from .ordershippings import OrderShippings
from .invoices import Invoices

# billing and shipping addresses
# billing address: linked to invoice_id
# shipping address: linked to ordershipping_id

class Addresses(AppModel):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    street_1 = models.CharField(max_length=255)
    street_2 = models.CharField(max_length=255, null=True, blank=True)
    street_3 = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=50)
    ordershipping_id = models.ForeignKey(OrderShippings, on_delete=models.CASCADE)
    invoice_id = models.ForeignKey(Invoices, on_delete=models.CASCADE)

    class Meta:
        db_table = 'addresses'