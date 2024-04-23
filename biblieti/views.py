# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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
                return render(request, 'dashboard.html')  # Redirige al usuario a la página de inicio después del inicio de sesión exitoso
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

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html', {'username': request.user.username})

def user_data(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        # Actualizar datos del usuario
        current_user = request.user
        user = User_ieti.objects.get(username=current_user)
        user.username = request.POST.get('name')
        user.mail = request.POST.get('email')
        user.save()
        pass
    print(request.user.username)
    return render(request, 'user_data.html', {'user': request.user})

def test(request):
    return render(request, 'test.html')