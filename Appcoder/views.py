from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def curso(request):

    curso = Curso(nombre= "Curso de python", comision =1225)
    curso.save()
    texto= f"Curso creado  nombre : {curso.nombre}, comision :{curso.comision}"
    return HttpResponse(texto)



def inicio(request):
    return render(request,"Appcoder/inicio.html")

def cursos(request):
    return render(request,"Appcoder/cursos.html")

def profesores(request):
    return render(request,"Appcoder/profesores.html")

def estudiantes(request):
    return render(request,"Appcoder/estudiante.html")


def entregables(request):
    return render(request,"Appcoder/entregable.html")

