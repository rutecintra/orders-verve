from django.db import models

# standard fields for tables

class AppModel(models.Model):
    title = models.CharField(max_length=256, null=False)
    fulltitle = models.CharField(max_length=520, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    default = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    order = models.IntegerField(null=True, blank=True)
    system = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=False)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(null=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True  # Define como uma classe abstrata para não criar uma tabela no banco


class RelationshipModel(models.Model):
    active = models.BooleanField(default=True)
    default = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    order = models.IntegerField(null=True, blank=True)
    system = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True