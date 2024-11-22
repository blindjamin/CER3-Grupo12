from django.contrib.auth.models import AbstractUser
from django.db import models

# Modelo de Usuario (Extendiendo el sistema de usuarios de Django)
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('docente', 'Docente'),
        ('estudiante', 'Estudiante'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='estudiante')
    is_active = models.BooleanField(default=True)

# Modelo de Evento
class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('inicio_semestre', 'Inicio de Semestre'),
        ('fin_semestre', 'Fin de Semestre'),
        ('inicio_inscripcion', 'Inicio de Inscripción de Asignaturas'),
        ('fin_inscripcion', 'Fin de Inscripción de Asignaturas'),
        ('receso', 'Receso Académico'),
        ('feriado_nacional', 'Feriado Nacional'),
        ('feriado_regional', 'Feriado Regional'),
        ('inicio_solicitudes', 'Inicio de Plazos de Solicitudes Administrativas'),
        ('fin_solicitudes', 'Fin de Plazos de Solicitudes Administrativas'),
        ('inicio_beneficios', 'Inicio de Plazos para la Gestión de Beneficios'),
        ('fin_beneficios', 'Fin de Plazos para la Gestión de Beneficios'),
        ('ceremonia_titulacion', 'Ceremonia de Titulación o Graduación'),
        ('reunion_consejo', 'Reunión de Consejo Académico'),
        ('taller_charla', 'Talleres y Charlas'),
        ('orientacion', 'Día de Orientación para Nuevos Estudiantes'),
        ('extracurricular', 'Eventos Extracurriculares'),
        ('inicio_clases', 'Inicio de Clases'),
        ('ultimo_dia_clases', 'Último Día de Clases'),
        ('puertas_abiertas', 'Día de Puertas Abiertas'),
        ('suspension_completa', 'Suspensión de Actividades Completa'),
        ('suspension_parcial', 'Suspensión de Actividades Parcial'),
    ]
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.CharField(max_length=30, choices=EVENT_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    is_official = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f"{self.title} ({self.get_type_display()})"
    
     #Modelo de Feriado
class Holiday(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    region = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Modelo de Notificación
class Notification(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación para {self.event.title}"
    
# Modelo de Revisión
class Review(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='review')
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    comments = models.TextField()
    status = models.CharField(max_length=20, choices=Event.STATUS_CHOICES)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Revisión de {self.event.title}"