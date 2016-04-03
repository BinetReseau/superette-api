from rest_framework import viewsets, decorators

from platalbank_core.serializers import UserSerializer
from rest_framework.response import Response

from platalbank_core.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @decorators.list_route()
    def me(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
