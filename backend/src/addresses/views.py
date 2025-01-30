from django.shortcuts import render
from rest_framework import viewsets
from .models import Addresses
from .serializers import AddressesSerializer

class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer
