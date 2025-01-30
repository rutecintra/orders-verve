from django.db import models
from src.models.appmodel import AppModel

# product categories
# "level" indicates the position of the category in the tree

class Categories(AppModel):
    level = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'categories'