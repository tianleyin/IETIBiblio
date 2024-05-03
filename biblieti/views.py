# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
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
    page_title = "CERCA - "  # Definir el título dinámico de la página
    return render(request, 'search_product.html', {'page_title': page_title})

def dashboard(request, notification=None, notificationMsg=None):
    page_title = "PANELL - "
    if not request.user.is_authenticated:
        return redirect('login')
    if request.session.get('notification') is not None:
        notification = request.session.get('notification')
        notificationMsg = request.session.get('notificationMsg')
        request.session.pop('notification')
        request.session.pop('notificationMsg')
        return render(request, 'dashboard.html', {'user': request.user, 'notification': notification, 'notificationMsg': notificationMsg, 'page_title': page_title})
    return render(request, 'dashboard.html', {'user': request.user, 'page_title': page_title})

def loans(request):
    page_title = "Préstecs - "
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.role == "librarian" and not request.user.role == "superadmin":
        return redirect('dashboard')
    
    data = {}
    message_list = messages.get_messages(request)
    for message in message_list:
        data['info'] = True
        data['infoMsg'] = message
    return render(request, "loans.html", {'data':data, 'page_title':page_title})

def loans_form(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.role == "librarian" and not request.user.role == "superadmin":
        return redirect('dashboard')
    return render(request, "loans_form.html")
    
def return_loan(request):
    page_title = "RETORNAR - "
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.role == "librarian" and not request.user.role == "superadmin":
        return redirect('dashboard')
    
    data = {}
    return render(request, "return_loan.html", {'data':data, 'page_title':page_title})


def user_data(request):
    page_title = "PERFIL - "
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
    return render(request, 'user_data.html', {'user': request.user, 'page_title':page_title})

def login_view(request):
    data = {}
    page_title = "INICI - "
    if request.method == "POST":
        print(request.POST)
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
                action = "succesful login of " + username
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
    return render(request, "registration/login.html", {'data': data, 'page_title': page_title})

def import_csv(request):
    page_title = "IMPORTAR CSV - "
    data = {}

    if request.method == 'POST':
        form = fileForm(request.POST, request.FILES)
        if form.is_valid():
            fileData = request.FILES.get('file')
            print(fileData)
            #rows = fileData.read().split('\n')
            for row in fileData:
                row = row.decode('utf-8')
                row = str(row).splitlines()
                row = row[0].split(',')
                print(row)
                #print(User_ieti.objects.filter(email=row[1]).exists())
                if (User_ieti.objects.filter(email=row[1]).exists()):
                    if data.get('warning') is None:
                        data['warning'] = True
                        data['warningMsg'] = "Les adreces de correu electrònic següents ja estan registrades:\\n"
                    data['warningMsg'] += row[1] + "\\n"
                    continue
                try:
                    user = User_ieti.objects.create(username=row[0], email=row[1], first_name=row[2], last_name=row[3], role=row[4], date_of_birth=row[5])
                    user.save()
                    if data.get('info') is None:
                        data['info'] = True
                        data['infoMsg'] = "S'han afegit correctament els següents usuaris:\\n"
                    data['infoMsg'] += row[1] + "\\n"
                except Exception as e:
                    print(e)
                    if data.get('error') is None:
                        data['error'] = True
                        data['errorMsg'] = "S'ha produït un error en la importació dels següents usuaris:\\n"
                    data['errorMsg'] += row[1] + "\\n"
                    continue
            if data.get('error'):
                data['errorMsg'] += "Si us plau, revisa els camps i torna a intentar-ho."
                #product = Product.objects.create(ISBN=row[0], name=row[1], author=row[2], publication_year=row[3], price=row[4], availability=row[5])
                #product.save()
    else:
        form = fileForm()
    data['form'] = form
    print(data)
    data['page_title'] = page_title
    return render(request, 'import_csv.html', page_title)

def add_user(request):
    page_title = "AFEGIR USUARI - "
    if request.method == "POST":
        if User_ieti.objects.filter(email=request.POST.get("email")).exists():
            return render(request, 'add_user.html', {"error": True, "errorMsg": "Aquest correu electrònic ja està registrat."})
        username = request.POST.get("name")
        email = request.POST.get("email")
        role = request.POST.get("role")
        cycle = request.POST.get("cycle")
        User_ieti.objects.create(username=username, email=email, role=role, cycle=cycle, password="Password12345")
    return render(request, 'add_user.html', {'page_title':page_title})

def edit_user_list(request):
    page_title = "EDITAR USUARI"  # Definir el título de la página
    data = {"users": list(User_ieti.objects.all())}
    return render(request, 'edit_user_list.html', {'page_title': page_title, **data})

def edit_user_form(request, email):
    user = User_ieti.objects.get(email=email)
    if request.method == "POST":
        user.username = request.POST.get("name")
        user.email = request.POST.get("email")
        user.role = request.POST.get("role")
        user.cycle = request.POST.get("cycle")
        user.save()
        request.session['notification'] = 'info'
        request.session['notificationMsg'] = 'Dades actualitzades correctament.'
        return redirect('edit_user_list')
    data = {"user": user}
    return render(request, 'edit_user_form.html', data)

def test(request):
    return render(request, 'test.html')
