from rest_framework import viewsets

from platalbank_core.models import FrankizUser
from platalbank_core.serializers import FrankizUserSerializer

class FrankizUserViewSet(viewsets.ModelViewSet):
    queryset = FrankizUser.objects.all()
    serializer_class = FrankizUserSerializer
