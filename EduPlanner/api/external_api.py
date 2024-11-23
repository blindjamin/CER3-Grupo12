import requests
from api.models import Feriado
from datetime import datetime


def obtener_feriados():
    url = "https://calendarific.com/api/v2/holidays"
    params = {
        "api_key": "4dlrihgSzDp6to2fNCTTHftITbijBu4c",
        "country": "CL",
        "year": "2024",
    }
    print("Enviando solicitud a la API...")
    print(f"URL: {url}")
    print(f"Parámetros: {params}")
    try:
        response = requests.get(url, params=params)
        print(f"Código de estado: {response.status_code}")
        print(f"Contenido: {response.text}")
        response.raise_for_status()
        data = response.json()
        return data.get("response", {}).get("holidays", [])
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None
    except ValueError as e:
        print(f"Error al procesar JSON: {e}")
        return None

def guardar_feriados(feriados):
    """
    Guarda los feriados en la base de datos.
    """
    for feriado in feriados:
        try:
            iso_date = feriado["date"]["iso"]
            date = iso_date.split('T')[0]  # Asegúrate de extraer solo la fecha
            Feriado.objects.get_or_create(
                name=feriado["name"],
                date=date,
                region=feriado.get("region", None)
            )
        except Exception as e:
            print(f"Error al procesar el feriado {feriado['name']}: {e}")

