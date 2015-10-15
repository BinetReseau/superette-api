from rest_framework import viewsets

from platalbank_core.models import Account
from platalbank_core.serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
