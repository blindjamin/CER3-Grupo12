from django import forms
from api.models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['title', 'description', 'start_date', 'end_date', 'type', 'status', 'is_official']
