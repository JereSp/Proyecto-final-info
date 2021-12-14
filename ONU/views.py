from django.http import HttpResponse
from django.template import Template, Context
from pathlib import Path
import os
from django.shortcuts import render

BASE_DIR = os.path.dirname(__file__)

def bienvenida(request):
    return HttpResponse("Bienvenido a nuestra pagina")

def contenidoExterno(request):
    plantillaExterna = open(os.path.join(BASE_DIR,"./templates/index.html"))
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def login(request):
    plantillaLogin = open(os.path.join(BASE_DIR,"./templates/login.html"))
    template = Template(plantillaLogin.read())
    plantillaLogin.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
