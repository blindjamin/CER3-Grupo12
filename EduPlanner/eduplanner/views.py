from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .models import Event, Holiday
from .forms import EventForm

# Mixin para verificar si el usuario es administrador
def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

class AdminRequiredMixin:
    @method_decorator(login_required)
    @method_decorator(user_passes_test(is_admin))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# Vista para listar eventos
class EventListView(ListView):
    model = Event
    template_name = 'admin/events_list.html'  # Template para listar eventos
    context_object_name = 'events'

# Vista para crear un evento
class EventCreateView(AdminRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'admin/event_form.html'
    success_url = reverse_lazy('events_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Asigna el usuario actual como creador
        return super().form_valid(form)

# Vista para actualizar un evento
class EventUpdateView(AdminRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'admin/event_form.html'
    success_url = reverse_lazy('events_list')

# Vista para ver el detalle de un evento
class EventDetailView(DetailView):
    model = Event
    template_name = 'admin/event_detail.html'  # Template para mostrar el detalle
    context_object_name = 'event'

# Vista para eliminar un evento
class EventDeleteView(AdminRequiredMixin, DeleteView):
    model = Event
    template_name = 'admin/event_confirm_delete.html'  # Template para confirmar eliminación
    success_url = reverse_lazy('events_list')

# Vista para mostrar el calendario consolidado
class CalendarPreviewView(TemplateView):
    template_name = 'calendar_preview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.all()
        holidays = Holiday.objects.all()

        # Combinar eventos y feriados, ordenados por fecha
        calendar = sorted(
            list(events) + list(holidays),
            key=lambda x: x.start_date if hasattr(x, 'start_date') else x.date
        )
        context['calendar'] = calendar
        return context
