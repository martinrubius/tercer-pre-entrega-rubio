from django import forms

class PacienteFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()
    dni= forms.IntegerField()
    
class MedicoFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    especialidad= forms.CharField(max_length=30)
    
class TurnoFormulario(forms.Form):
    id= forms.IntegerField()
    dni= forms.IntegerField()
    fecha = forms.DateField()
    apellido= forms.CharField(max_length=50)