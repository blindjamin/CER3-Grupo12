from django.contrib import admin
from django.urls import path,include
from .views import ListaEventosView, CrearEventoView,ActualizarEventoView,DetalleEventoView,EliminarEventoView,VistaCalendarioConsolidado
from api.views import home


urlpatterns = [

    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('eventos/', include('eduplanner.urls')),
    path('eventos/', ListaEventosView.as_view(), name='eventos_lista'),
    path('eventos/crear/', CrearEventoView.as_view(), name='crear_evento'),
    path('eventos/<int:pk>/editar/', ActualizarEventoView.as_view(), name='editar_evento'),
    path('eventos/<int:pk>/', DetalleEventoView.as_view(), name='detalle_evento'),
    path('eventos/<int:pk>/eliminar/', EliminarEventoView.as_view(), name='eliminar_evento'),
    path('calendario/', VistaCalendarioConsolidado.as_view(), name='calendario_consolidado')
]