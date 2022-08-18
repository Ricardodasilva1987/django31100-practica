from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def curso(request):

    curso = Curso(nombre= "Curso de python", comision =1225)
    curso.save()
    texto= f"Curso creado  nombre : {curso.nombre}, comision :{curso.comision}"
    return HttpResponse(texto)