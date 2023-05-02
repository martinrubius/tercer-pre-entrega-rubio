from django.urls import path
from app1 import views
urlpatterns = [
    
    path('', views.inicio, name="Inicio"), 
    path('medicos', views.medicos, name="Medicos"),
    path('pacientes', views.pacientes, name="Pacientes"),
    path('turnos', views.turnos, name="Turnos"),
    path('medicoFormulario', views.medicoFormulario, name="MedicoFormulario"),
    path('pacienteFormulario', views.pacienteFormulario, name="PacienteFormulario"),
    path('turnoFormulario', views.turnoFormulario, name="TurnoFormulario"),
    path('leerMedicos', views.leerMedicos, name="LeerMedicos"),
    path('leerPacientes', views.leerPacientes, name="leerPacientes"),
    path('leerTurnos', views.leerTurnos, name="leerTurnos"),
    path('buscarMedicos', views.busquedaMedico, name="buscarMedicos"),
    path('buscar/',views.buscar),

]