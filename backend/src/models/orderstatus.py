from django.db import models
from .appmodel import AppModel
from .integrations import Integrations

# intern order statuses

class OrderStatus(AppModel):
    suspend = models.BooleanField(default=False)

    class Meta:
        db_table = 'orderstatus'