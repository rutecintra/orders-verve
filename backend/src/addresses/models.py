from django.db import models
from models.appmodel import AppModel

# billing and shipping addresses
# billing address: linked to invoice_id
# shipping address: linked to ordershipping_id

class Addresses(AppModel):
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    street_1 = models.CharField(max_length=255, null=True, blank=True)
    street_2 = models.CharField(max_length=255, null=True, blank=True)
    street_3 = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    ordershippings = models.ForeignKey("orders.OrderShippings", on_delete=models.CASCADE)
    invoices = models.ForeignKey("invoices.Invoices", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'addresses'
