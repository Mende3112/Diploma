from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .utils import render_to_pdf


def index(request):
    return render(request, 'index.html',{
        #Contexto
        'message': 'Bienvenido a Generador de Diploma',
        'parrafo': 'Debes ingresar tu nombre  para poder obtener tu diploma de participación'
    })
def pdf(request):
    #mensaje = "Nombre guardado: %r" %request.GET['nombre']
    mensaje=request.GET['nombre']
    return render(request,'diploma.html',{
        'nombre':mensaje
    })
    #return HttpResponse(mensaje)

"""Render pdf"""
"""class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('template/diploma.html',pdf())
        return HttpResponse(pdf, content_type='application/pdf')"""

def pdf2(request, *args, **kwargs):
    mensaje=request.GET['nombre']
    pdf = render_to_pdf('diploma.html', {
        'nombre': mensaje
    })
    return HttpResponse(pdf, content_type='application/pdf')