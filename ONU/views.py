from django.http import HttpResponse
from django.template import Template, Context
from pathlib import Path
import os
from django.shortcuts import render

import requests

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

def main(request):
    plantillaMain = open(os.path.join(BASE_DIR,"./templates/main.html"))
    template = Template(plantillaMain.read())
    plantillaMain.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def posts(request):
    req = requests.get('http://127.0.0.1:8000/api/posts/?format=json')
    data = []
    if (req.status_code == 200):
        data = req.json()
        print(data)

    html = open(os.path.join(BASE_DIR, "./templates/posts.html"))
    template = Template(html.read())
    html.close()
    context = Context({ 'data' : data })
    doc = template.render(context)
    return HttpResponse(doc)    

def postBody(request, postid):
    print(postid)
    req = requests.get(f'http://127.0.0.1:8000/api/posts/{postid}?format=json')
    data = []
    if (req.status_code == 200):
        data = req.json()
        print(data)
    
    plantillaBodyPost = open(os.path.join(BASE_DIR, "./templates/bodypost.html"))
    template = Template(plantillaBodyPost.read())
    plantillaBodyPost.close()
    context = Context({ 'data' : data })
    doc = template.render(context)
    return HttpResponse(doc)
    