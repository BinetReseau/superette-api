from rest_framework import viewsets, decorators

from platalbank_core.models import Transaction
from platalbank_core.serializers import TransactionSerializer, FlatTransactionSerializer
from rest_framework.response import Response

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    filter_fields = ('state', 'event', 'credited_account', 'debited_account',)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'destroy']:
            return FlatTransactionSerializer
        return TransactionSerializer

    @decorators.detail_route()
    def cancel(self, request, pk=None):
        try:
            t = Transaction.objects.get(pk=pk)
            if t.state != Transaction.ABORTED:
                t.state = Transaction.ABORTED
                if t.debited_account.pk != t.credited_account.pk:
                    t.credited_account.balance -= t.amount
                    t.debited_account.balance += t.amount
                    t.credited_account.save()
                    t.debited_account.save()
                print(t.state)
                t.save()
                return Response(204)
            else:
                return Response("Already canceled", 400)
        except Exception as e:
            print (e.message)
            return Response(400)
