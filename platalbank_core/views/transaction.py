from rest_framework import viewsets

from platalbank_core.models import Transaction
from platalbank_core.serializers import TransactionSerializer, FlatTransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    filter_fields = ('state', 'event', 'credited_account', 'debited_account',)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'destroy']:
            return FlatTransactionSerializer
        return TransactionSerializer
