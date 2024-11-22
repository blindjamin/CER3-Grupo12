from django.contrib import admin
from .models import User, Evento, Feriado, Notificacion, Revision

admin.site.register(User)
admin.site.register(Evento)
admin.site.register(Feriado)
admin.site.register(Notificacion)
admin.site.register(Revision)
