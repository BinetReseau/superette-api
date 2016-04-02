from rest_framework import viewsets, decorators

from django.contrib.auth.models import User
from platalbank_core.serializers import UserSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @decorators.list_route()
    def me(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
