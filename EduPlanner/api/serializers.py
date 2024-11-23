from rest_framework import serializers
from .models import Evento, Feriado, Notificacion, Revision

# Serializer para Event
class EventoSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Evento
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'type', 'type_display', 'status', 'is_official', 'created_by']
        read_only_fields = ['id', 'created_by', 'type_display']

# Serializer para Holiday
class FreiadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feriado 
        fields = ['id', 'name', 'date', 'region']
        read_only_fields = ['id']

# Serializer para Notification
class NotificacionSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source='event.title', read_only=True)

    class Meta:
        model = Notificacion
        fields = ['id', 'event', 'event_title', 'message', 'created_at']
        read_only_fields = ['id', 'created_at', 'event_title']

# Serializer para Review
class RevisionSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source='event.title', read_only=True)
    reviewed_by_username = serializers.CharField(source='reviewed_by.username', read_only=True)

    class Meta:
        model = Revision
        fields = ['id', 'event', 'event_title', 'reviewed_by', 'reviewed_by_username', 'comments', 'status', 'reviewed_at']
        read_only_fields = ['id', 'reviewed_at', 'event_title', 'reviewed_by_username']
