from django.contrib import admin
from .models import HojaDeVida, Certificado


@admin.register(HojaDeVida)
class HojaDeVidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')