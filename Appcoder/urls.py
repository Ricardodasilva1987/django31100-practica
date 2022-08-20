from django.urls import path
from .views import *

urlpatterns = [
    path('curso/', curso),
    path('profesores/', profesores),
    path('estudiante/', estudiantes),
    path('entregable/', entregables),
    path('cursos/', cursos),
    path('', inicio), #Se coloca vacio para que sea la paginia de inicio y no necesita ruta

]