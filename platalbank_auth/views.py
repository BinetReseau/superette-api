from rest_framework import viewsets

from platalbank_auth.models import User
from platalbank_auth.serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
