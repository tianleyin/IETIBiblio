# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone
import re


def validar_contrasena(contrasena):
    # Longitud entre 8 y 16 caracteres
    if not 8 <= len(contrasena) <= 16:
        return False

    # Al menos una letra mayúscula
    if not re.search(r'[A-Z]', contrasena):
        return False

    # Al menos una letra minúscula
    if not re.search(r'[a-z]', contrasena):
        return False

    # Al menos un número
    if not re.search(r'\d', contrasena):
        return False

    # Al menos un símbolo
    if not re.search(r'[!@#$%^&*()-_=+{};:,.<>?]', contrasena):
        return False

    return True


def landing_page(request):
    return render(request, 'landing_page.html')

def busqueda(request):
    return render(request, 'search_product.html')

def dashboard(request, notification=None, notificationMsg=None):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.session.get('notification') is not None:
        notification = request.session.get('notification')
        notificationMsg = request.session.get('notificationMsg')
        request.session.pop('notification')
        request.session.pop('notificationMsg')
        return render(request, 'dashboard.html', {'username': request.user.username, 'notification': notification, 'notificationMsg': notificationMsg})
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
        user.school = request.POST.get('school')
        user.cycle = request.POST.get('cycle')
        user.save()
        request.session['notification'] = 'info'
        request.session['notificationMsg'] = 'Dades actualitzades correctament.'
        return redirect('dashboard')
    print(request.user.username)
    return render(request, 'user_data.html', {'user': request.user})

def login_view(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User_ieti.objects.get(username=username)
            print(password)
            if user is not None and validar_contrasena(password) and check_password(password, user.password):
                login(request, user)

                # save log of login user
                current_date = timezone.now()
                level = "info"
                client_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('HTTP_CLIENT_IP') or request.META.get('REMOTE_ADDR')
                action = "succesfull login of " + username
                current_page = "landing_page"

                log_entry = Logs.objects.create(date=current_date, type=level, client_ip=client_ip, action=action, current_page=current_page)
                log_entry.save()

                return redirect("dashboard")
            else:
                data['error'] = True
                if not validar_contrasena(password):
                    data['errorMsg'] = "La contrasenya ha de tenir entre 8 i 16 caràcters, com a mínim una lletra majúscula, una lletra minúscula, un número i un símbol."
                else:
                    data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
        except:
            data['error'] = True
            data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
    return render(request, "registration/login.html", data)

def test(request):
    return render(request, 'test.html')
