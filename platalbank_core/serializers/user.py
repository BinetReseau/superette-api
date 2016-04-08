from rest_framework import serializers
from platalbank_core.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'room', 'phone', 'promo', 'is_staff')

class ShortUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'email', 'username', 'first_name', 'last_name')
