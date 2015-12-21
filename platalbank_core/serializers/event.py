from rest_framework import serializers

from platalbank_core.models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'id', 'label', 'through_khube', 'writable')

class ShortEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'id', 'label')
