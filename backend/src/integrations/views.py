from django.shortcuts import render
from rest_framework import viewsets
from .models import Integrations
from .serializers import IntegrationsSerializer

class IntegrationsViewSet(viewsets.ModelViewSet):
    queryset = Integrations.objects.all()
    serializer_class = IntegrationsSerializer
