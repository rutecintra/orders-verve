from django.shortcuts import render
from rest_framework import viewsets
from .models import Customers
from .serializers import CustomersSerializer

class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
