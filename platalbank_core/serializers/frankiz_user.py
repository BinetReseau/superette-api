from rest_framework import serializers

from platalbank_core.models import FrankizUser


class FrankizUserListSerializer(serializers.ListSerializer):
    pass

class FrankizUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FrankizUser
        fields = ('url', 'id', 'hruid', 'first_name', 'last_name', 'email', 'phone', 'room', 'promo')
        list_serializer_class = FrankizUserListSerializer
