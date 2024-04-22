# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def landing_page(request):
    return render(request, 'biblieti/landing_page.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        User = authenticate(request, email=email, password=password)
        if User is not None:
            login(request, User)
            return redirect('dashboard')  # Redirigir a la página de inicio después del inicio de sesión exitoso
        else:
            # Mostrar un mensaje de error de inicio de sesión en caso de credenciales incorrectas
            return render(request, 'biblieti/landing_page.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'biblieti/landing_page.html')
