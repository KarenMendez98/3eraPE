from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 




def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal de Trotamundos")

def inicioApp(request):
    return render(request, "AppKaren/inicio.html",{"avatar":obtenerAvatar(request)})

def destinos(request):
    return render(request, "AppKaren/destinos.html")

def paquetes(request):
    return render(request, "AppKaren/paquetes.html")

def about(request):
    return render(request, "AppKaren/about.html")

def todo(request):
    return render(request, "AppKaren/todo.html",{"avatar":obtenerAvatar(request)})

def busquedaActividad(request):
    return render(request, "AppKaren/busquedaActividad.html",{"avatar":obtenerAvatar(request)})

def agregarAvatar(request):
    return render(request, "AppKaren/AgregarAvatar.html",{"avatar":obtenerAvatar(request)})

def paris(request):
    return render(request, "AppKaren/paris.html",{"avatar":obtenerAvatar(request)})
def puntaCana(request):
    return render(request, "AppKaren/puntaCana.html",{"avatar":obtenerAvatar(request)})
def miami(request):
    return render(request, "AppKaren/miami.html",{"avatar":obtenerAvatar(request)})
def egipto(request):
    return render(request, "AppKaren/egipto.html",{"avatar":obtenerAvatar(request)})
def hongKong(request):
    return render(request, "AppKaren/hongKong.html",{"avatar":obtenerAvatar(request)})
def newZeland(request):
    return render(request, "AppKaren/newZeland.html",{"avatar":obtenerAvatar(request)})



###
def paquetes(request):    
    if request.method =="POST":
        form = PaqueteForm(request.POST)
        if form.is_valid():
            paquete = Paquete()
            paquete.lugar = form.cleaned_data["lugar"]
            paquete.cant_dias = form.cleaned_data["cant_dias"]         
            paquete.cant_pasajeros = form.cleaned_data["cant_pasajeros"]
            paquete.save()
            form = PaqueteForm()
    else:
        form = PaqueteForm()

    paquetes = Paquete.objects.all()  

    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url          
    return render(request, "AppKaren/paquetes.html", {"paquetes": paquetes, "form": form,"avatar":avatar})



def destinos(request):
    
    if request.method =="POST":
        form = VisitaGForm(request.POST)
        if form.is_valid():
            visita = Visita()
            visita.tipo = form.cleaned_data["tipo"]
            visita.ciudad = form.cleaned_data["ciudad"]         
            visita.save()
            form = VisitaGForm()
    else:
        form = VisitaGForm()

    visitas = Visita.objects.all()  

    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url          
    return render(request, "AppKaren/destinos.html", {"visitas": visitas, "form": form, "avatar":avatar} )

###

def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"


@login_required
def busquedaActividad(request):
    return render(request, "AppKaren/busquedaActividad.html", {"avatar":obtenerAvatar(request)})


@login_required
def buscar(request):
    ciudad = request.GET["ciudad"]

    if ciudad!="":
        visitas= Visita.objects.filter(ciudad = ciudad)
        return render(request, "AppKaren/resultadosBusqueda.html", {"visitas": visitas, "ciudad": ciudad})
    
    else:
        return render(request, "AppKaren/busquedaActividad.html", {"mensaje": "Ingrese una ciudad válida", "avatar":obtenerAvatar(request)})


@login_required
def viajeros(request):
    
    if request.method =="POST":
        form = PasajeroForm(request.POST)
        if form.is_valid():
            viajero = Viajero()
            viajero.nombre= form.cleaned_data["nombre"]
            viajero.apellido = form.cleaned_data["apellido"]         
            viajero.email = form.cleaned_data["email"]
            viajero.destino= form.cleaned_data["destino"]
            viajero.save()
            form = PasajeroForm()
    else:
        form = PasajeroForm()

    viajeros = Viajero.objects.all()
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url          
    return render(request, "AppKaren/viajeros.html", {"viajeros": viajeros, "form": form, "avatar":avatar})



@login_required
def eliminarViajero(request, id):
    viajero=Viajero.objects.get(id=id)
    print(viajero)
    viajero.delete()
    viajeros=Viajero.objects.all()
    form = PasajeroForm()
    return render(request, "AppKaren/Viajeros.html", {"viajeros": viajeros, "mensaje": "Viajero eliminado correctamente", "form": form})


@login_required
def editarViajero(request, id):
    viajero=Viajero.objects.get(id=id)
    if request.method=="POST":
        form= PasajeroForm(request.POST)
        if form.is_valid():
            
            info=form.cleaned_data
            
            viajero.nombre=info["nombre"]
            viajero.apellido=info["apellido"]
            viajero.email=info["email"]
            viajero.destino=info["destino"]

            viajero.save()
            viajeros=Viajero.objects.all()
            form = PasajeroForm()
            return render(request, "AppKaren/Viajeros.html" ,{"viajeros":viajeros, "mensaje": "Viajero editado correctamente", "form": form})
        pass
    else:
        formulario= PasajeroForm(initial={"nombre":viajero.nombre, "apellido":viajero.apellido, "email":viajero.email, "destino":viajero.destino})
        return render(request, "AppKaren/editarViajero.html", {"form": formulario, "viajero": viajero})
    


####

def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppKaren/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppKaren/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppKaren/register.html", {"form": form})


@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppKaren/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppKaren/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url          
        return render(request, "AppKaren/editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "avatar":avatar})

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppKaren/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppKaren/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppKaren/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})
    


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppKaren/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppKaren/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppKaren/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppKaren/login.html", {"form": form})
    

    ###

class PaqueteList(LoginRequiredMixin, ListView):#vista usada para LISTAR
    model= Paquete
    template_name= "AppKaren/paquetes.html"

class PaqueteCreacion(LoginRequiredMixin, CreateView):#vista usada para CREAR
    model= Paquete
    success_url= reverse_lazy("paquetes_list")
    fields=['lugar', 'cant_pasajeros', 'cant_dias']

class PaqueteDetalle(LoginRequiredMixin, DetailView): #vista usada para MOSTRAR DATOS
    model= Paquete
    template_name="Appcoder/paquete_detalle.html"

class PaqueteDelete(LoginRequiredMixin, DeleteView):#vista usada para ELIMINAR
    model=Paquete
    success_url= reverse_lazy("paquete_list")

class PaqueteUpdate(LoginRequiredMixin, UpdateView):#vista usada para EDITAR
    model = Paquete
    success_url = reverse_lazy('paquete_list')
    fields=['lugar', 'cant_pasajeros', 'cant_dias']
  

