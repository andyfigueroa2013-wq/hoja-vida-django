from django.shortcuts import render
from .models import HojaDeVida, Certificado

def inicio(request):
    hoja = HojaDeVida.objects.first()
    certificados = Certificado.objects.all()

    return render(request, 'cv/inicio.html', {
        'hoja': hoja,
        'certificados': certificados
    })


def certificados(request):
    certificados = Certificado.objects.all()
    return render(request, 'cv/certificados.html', {
        'certificados': certificados
    })
