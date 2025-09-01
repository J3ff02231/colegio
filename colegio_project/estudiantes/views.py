from django.shortcuts import render, redirect
from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'edad', 'correo']

def formulario_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()  # 👈 guarda en PostgreSQL
            return redirect('formulario_estudiante')
    else:
        form = EstudianteForm()
    return render(request, 'formulario.html', {'form': form})
