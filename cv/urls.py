from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('certificados/', views.certificados, name='certificados'),
]