from django.db import models
from src.models.appmodel import AppModel

# carrier registration, in the future this table will be integrated with the freight table

class Logistics(AppModel):
    carriercode = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'logistics'