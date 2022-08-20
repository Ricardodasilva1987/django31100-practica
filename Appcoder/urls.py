from django.urls import path
from .views import *

urlpatterns = [
    path('curso/', curso, name ="curso"),
    path('profesores/', profesores, name ="profesores"),
    path('estudiante/', estudiantes, name ="estudiantes"),
    path('entregable/', entregables, name="entregables"),
    path('cursos/', cursos, name = "cursos"),
    path('', inicio, name ="inicio"), #Se coloca vacio para que sea la paginia de inicio y no necesita ruta

]