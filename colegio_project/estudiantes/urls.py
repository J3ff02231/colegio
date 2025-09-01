from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.formulario_estudiante, name='formulario_estudiante'),
]
