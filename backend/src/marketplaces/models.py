from django.db import models
from src.models.appmodel import AppModel
from src.integrations.models import Integrations

# sales channel

class Marketplaces(AppModel):
    integrations = models.ForeignKey(Integrations, on_delete=models.CASCADE)

    class Meta:
        db_table = 'marketplaces'