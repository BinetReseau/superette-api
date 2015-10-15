from rest_framework import viewsets

from platalbank_core.models import Transaction
from platalbank_core.serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
