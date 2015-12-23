from rest_framework import serializers

from platalbank_core.models import Transaction

from . import ShortAccountSerializer, ShortEventSerializer

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Transaction
        fields = ('url', 'id', 'state', 'amount', 'label', 'debited_account', 'credited_account', 'event', 'created', 'last_modified')

    debited_account  = ShortAccountSerializer()
    credited_account = ShortAccountSerializer()
    event            = ShortEventSerializer()

class FlatTransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Transaction
        fields = ('url', 'id', 'state', 'amount', 'label', 'debited_account', 'credited_account', 'event', 'created', 'last_modified')
