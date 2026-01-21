from django.db import models

# Create your models here.
class HojaDeVida(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    perfil = models.TextField()
    educacion = models.TextField()
    experiencia = models.TextField()
    habilidades = models.TextField()
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Certificado(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='certificados/', blank=True, null=True)
    pdf = models.FileField(upload_to='certificados/pdf/', blank=True, null=True)
    fecha = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
