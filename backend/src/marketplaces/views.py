from django.shortcuts import render
from rest_framework import viewsets
from .models import Marketplaces
from .serializers import MarketplacesSerializer

class MarketplacesViewSet(viewsets.ModelViewSet):
    queryset = Marketplaces.objects.all()
    serializer_class = MarketplacesSerializer
