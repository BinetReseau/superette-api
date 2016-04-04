from rest_framework import viewsets

from platalbank_core.models import Account
from platalbank_core.serializers import AccountSerializer, FlatAccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_fields = ('short_name', 'balance', 'owner')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'destroy']:
            return FlatAccountSerializer
        return AccountSerializer
