from rest_framework import serializers
from .models import Invoices

class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = '__all__'
