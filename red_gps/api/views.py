import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Ubicacion

def enviar_ubicacion(request):
    return render(request, "enviar_ubicacion.html")

@csrf_exempt 
def guardar_ubicacion(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            lat = data.get("latitud")
            lon = data.get("longitud")
            if lat and lon:
                Ubicacion.objects.create(latitud=lat, longitud=lon)
                return JsonResponse({"status": "ok", "message": "Ubicación guardada"})
            else:
                return JsonResponse({"status": "error", "message": "Faltan datos"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "error", "message": "Método no permitido"}, status=405)

def lista_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all().order_by("-fecha_hora")
    return render(request, "lista_ubicaciones.html", {"ubicaciones": ubicaciones})

def detalle_ubicacion(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    return render(request, "detalle_ubicacion.html", {"ubicacion": ubicacion})

def eliminar_ubicacion(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    ubicacion.delete()
    return render(request, "lista_ubicaciones.html", {"mensage": "Ubicación eliminada", "ubicaciones": ubicaciones})
