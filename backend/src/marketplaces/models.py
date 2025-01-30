from django.db import models
from models.appmodel import AppModel
from integrations.models import Integrations

# sales channel

class Marketplaces(AppModel):
    integrations = models.ForeignKey(Integrations, on_delete=models.CASCADE)

    class Meta:
        db_table = 'marketplaces'