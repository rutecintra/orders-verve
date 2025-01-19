from django.db import models
from .appmodel import AppModel
from .integrations import Integrations

# sales channel

class Marketplaces(AppModel):
    integration_id = models.ForeignKey(Integrations, on_delete=models.CASCADE)

    class Meta:
        db_table = 'marketplaces'