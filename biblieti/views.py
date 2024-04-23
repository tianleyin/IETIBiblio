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

def login_view(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User_ieti.objects.get(username=username)
            if user is not None:
                login(request, user)
                print(request.user)
                return redirect("dashboard")
            else:
                data['error'] = True
                data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
        except:
            data['error'] = True
            data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
    return render(request, "registration/login.html", data)

def test(request):
    return render(request, 'test.html')
