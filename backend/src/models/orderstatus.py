from django.db import models
from .appmodel import AppModel
from .integrations import Integrations

# order statuses linked to integrations

class OrderStatus(AppModel):
    integrations = models.ForeignKey(Integrations, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orderstatus'