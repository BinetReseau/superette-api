from rest_framework import viewsets

from platalbank_core.models import Event
from platalbank_core.serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
