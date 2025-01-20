from django.db import models
from .appmodel import AppModel

class Integrations(AppModel):
    apikey = models.CharField(max_length=255, null=True, blank=True)
    apiurl = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'integrations'