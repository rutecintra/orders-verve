from rest_framework import serializers
from .models import Integrations

class IntegrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrations
        fields = '__all__'
