from rest_framework import viewsets
from .models import Invoices
from .serializers import InvoicesSerializer

class InvoicesViewSet(viewsets.ModelViewSet):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer
