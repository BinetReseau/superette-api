from django.db import models
from rest_framework import serializers, viewsets

class Event(models.Model):
    label = models.CharField(max_length=1024)
    # if true, authorization requests will be sent to the khube, otherwise to the customer.
    through_khube = models.BooleanField()
    # whether new transactions can be added
    writable = models.BooleanField()
    # TODO: owner = models.ForeignKey("LegalPerson")

    def __str__(self):
        return self.label

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'id', 'label', 'through_khube', 'writable')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
