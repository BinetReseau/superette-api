from rest_framework import serializers

from platalbank_core.models import Account

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('url', 'id', 'balance', 'description', 'short_name')

class ShortAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('url', 'id', 'short_name')
