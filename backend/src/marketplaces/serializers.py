from rest_framework import serializers
from .models import Marketplaces

class MarketplacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplaces
        fields = '__all__'
