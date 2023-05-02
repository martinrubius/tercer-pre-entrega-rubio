from django.db import models

# Create your models here.

class Paciente(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | E-mail: {self.email} | DNI: {self.dni}"
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    dni= models.IntegerField()

class Medico(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | E-mail: {self.email} | Profesión: {self.especialidad}"
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    especialidad= models.CharField(max_length=30)

class Turno(models.Model):
    def __str__(self):
        return f"Fecha: {self.fecha} | DNI Paciente: {Paciente.dni} | Medico: {Medico.apellido}"
    Paciente.dni= models.IntegerField()
    fecha= models.DateField()
    Medico.apellido= models.BooleanField()