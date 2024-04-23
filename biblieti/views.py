# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def landing_page(request):
    return render(request, 'landing_page.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User_ieti.objects.get(mail=email)
            if check_password(password, user.password):
                # Usuario autenticado correctamente
                # Realiza el login del usuario
                return redirect('dashboard')  # Redirige al usuario a la página de inicio después del inicio de sesión exitoso
            else:
                # Contraseña incorrecta
                return render(request, 'landing_page.html', {'error': 'Credenciales inválidas, Contraseña Incorrecta'})
        except User_ieti.DoesNotExist:
            # Usuario no encontrado
            return render(request, 'landing_page.html', {'error': 'Credenciales inválidas, No existe el Usuario'})
    else:
        return render(request, 'landing_page.html')


def busqueda(request):
    return render(request, 'search_product.html')

def test(request):
    return render(request, 'test.html')

def dashboard(request):
    return render(request, 'dashboard.html')