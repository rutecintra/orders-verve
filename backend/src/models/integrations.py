from django.db import models
from .appmodel import AppModel

class Integrations(AppModel):
    apikey = models.CharField(max_length=255)

    class Meta:
        db_table = 'integrations'