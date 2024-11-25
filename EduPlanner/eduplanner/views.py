from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .forms import EventoForm
from api.models import Evento, Feriado

# Mixin para verificar si el usuario es administrador
def es_administrador(usuario):
    return usuario.is_authenticated and usuario.role == 'admin'

class AdministradorRequeridoMixin:
    @method_decorator(login_required)
    @method_decorator(user_passes_test(es_administrador))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# Vista para listar eventos
class ListaEventosView(ListView):
    model = Evento
    template_name = 'admin/eventos_lista.html'  # Template para listar eventos
    context_object_name = 'eventos'

# Vista para crear un evento
class CrearEventoView(AdministradorRequeridoMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'admin/evento_formulario.html'
    success_url = reverse_lazy('eventos_lista')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user  # Asigna el usuario actual como creador
        return super().form_valid(form)

# Vista para actualizar un evento
class ActualizarEventoView(AdministradorRequeridoMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'admin/evento_formulario.html'
    success_url = reverse_lazy('eventos_lista')

# Vista para ver el detalle de un evento
class DetalleEventoView(DetailView):
    model = Evento
    template_name = 'admin/evento_detalle.html'  # Template para mostrar el detalle
    context_object_name = 'evento'

# Vista para eliminar un evento
class EliminarEventoView(AdministradorRequeridoMixin, DeleteView):
    model = Evento
    template_name = 'admin/evento_confirmar_eliminacion.html'  # Template para confirmar eliminación
    success_url = reverse_lazy('eventos_lista')

# Vista para mostrar el calendario consolidado
class VistaCalendarioConsolidado(TemplateView):
    template_name = 'calendario_consolidado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        eventos = Evento.objects.all()
        feriados = Feriado.objects.all()

        # Combinar eventos y feriados, ordenados por fecha
        calendario = sorted(
            list(eventos) + list(feriados),
            key=lambda x: x.start_date if hasattr(x, 'start_date') else x.date
        )
        context['calendario'] = calendario
        return context
