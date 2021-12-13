from django.http import HttpResponse
from django.template import Template, Context

def bienvenida(request):
    return HttpResponse("Bienvenido a nuestra pagina")

def contenidoExterno(request):
    plantillaExterna = open("D:/informatorio/entorno/entornoinfo/ONU/ONU/templates/index.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def login(request):
    plantillaLogin = open("D:/informatorio/entorno/entornoinfo/ONU/ONU/templates/login.html")
    template = Template(plantillaLogin.read())
    plantillaLogin.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)