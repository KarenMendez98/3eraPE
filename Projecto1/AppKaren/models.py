from django.db import models
from django.contrib.auth.models import User


class Viajero(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    destino=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.destino}"    


class Paquete(models.Model):
    lugar= models.CharField(max_length=50)
    cant_pasajeros= models.CharField(max_length=50)
    cant_dias= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.lugar} {self.cant_pasajeros} {self.cant_dias}" 


class Visita(models.Model):
    tipo= models.CharField(max_length=50)
    ciudad= models.CharField(max_length=50)   

    def __str__(self):
        return f"{self.tipo} - {self.ciudad}"    
    

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)



