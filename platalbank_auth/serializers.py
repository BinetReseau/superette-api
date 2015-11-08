from rest_framework import serializers

from platalbank_auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "groups", "is_staff", "phone_number", "room")
