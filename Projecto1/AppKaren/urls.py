from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", inicioApp, name="inicioApp"),
    path("viajeros/", viajeros, name="viajeros"),
    path("destinos/", destinos, name="destinos"),
    path("paquetes/", paquetes, name="paquetes"),
    path("busquedaActividad/", busquedaActividad, name="busquedaActividad"),
    path("buscar/", buscar, name="buscar"),

    path("eliminarViajero/<id>", eliminarViajero, name="eliminarViajero"),
    path("editarViajero/<id>", editarViajero, name="editarViajero"),

    path("paquete/list/", PaqueteList.as_view(), name="paquete_list"),
    path('paquete/nuevo/', PaqueteCreacion.as_view(), name='paquete__crear'),
    path('paquete/<pk>', PaqueteDetalle.as_view(), name='paquete__detalle'),
    path('paquete/editar/<pk>', PaqueteUpdate.as_view(), name='paquete__editar'),
    path('paquete/borrar/<pk>', PaqueteDelete.as_view(), name='paquete__borrar'),


    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path('logout/', LogoutView.as_view(template_name="AppKaren/logout.html"), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('about/', about, name='about'),
    path('todo/', todo, name='todo'),
    path('paris/',paris, name="paris"),
    path('puntaCana/', puntaCana, name="puntaCana"),
    path('miami/', miami, name="miami"),
    path('egipto/', egipto, name="egipto"),
    path('hongKong/', hongKong, name="hongKong"),
    path('newZeland/', newZeland, name="newZeland")



]