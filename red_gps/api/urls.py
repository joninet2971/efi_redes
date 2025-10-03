from django.urls import path
from . import views

urlpatterns = [
    path("enviar/", views.enviar_ubicacion, name="enviar_ubicacion"),
    path("guardar/", views.guardar_ubicacion, name="guardar_ubicacion"),
    path("lista/", views.lista_ubicaciones, name="lista_ubicaciones"),
    path("detalle/<int:pk>/", views.detalle_ubicacion, name="detalle_ubicacion"),
    path("eliminar/<int:pk>/", views.eliminar_ubicacion, name="eliminar_ubicacion"),
]
