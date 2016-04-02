from rest_framework import serializers

from platalbank_core.models import Account
from .user import ShortUserSerializer

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('url', 'id', 'balance', 'description', 'short_name', 'owner')

    owner = ShortUserSerializer()

class ShortAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('url', 'id', 'short_name')

class FlatAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Account
        fields = ('url', 'id', 'balance', 'description', 'short_name', 'owner')
