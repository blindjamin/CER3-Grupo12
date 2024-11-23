from django.core.management.base import BaseCommand
from api.external_api import obtener_feriados

class Command(BaseCommand):
    help = "Sincroniza los feriados con la API externa"

    def handle(self, *args, **kwargs):
        try:
            feriados = obtener_feriados()
            if feriados:
                self.stdout.write(self.style.SUCCESS("Feriados sincronizados correctamente."))
            else:
                self.stdout.write(self.style.ERROR("No se pudo sincronizar con la API externa."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error al sincronizar feriados: {e}"))
