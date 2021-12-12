from django.http import HttpResponse
from django.template import Template, Context

def bienvenida(request):
    return HttpResponse("Bienvenido a nuestra pagina")

def contenidoExterno(request):
    plantillaExterna = open("D:/informatorio/entorno/entornoinfo/ONU/ONU/plantillas/index.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)