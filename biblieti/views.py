# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone

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
        return render(request, 'dashboard.html', {'user': request.user, 'notification': notification, 'notificationMsg': notificationMsg})
    return render(request, 'dashboard.html', {'user': request.user})

def loans(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.role == "librarian" and not request.user.role == "superadmin":
        return redirect('dashboard')
    return render(request, "loans.html")

def loans_form(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.role == "librarian" and not request.user.role == "superadmin":
        return redirect('dashboard')
    return render(request, "loans_form.html")
    

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
            if user is not None and check_password(password, user.password):
                login(request, user)
                print(request.user)

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
                data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
        except:
            data['error'] = True
            data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
    return render(request, "registration/login.html", data)

def import_csv(request):
    data = {}
    if request.method == 'POST':
        # Importar csv
        print(request.POST.get("data"))
        rows = request.POST.get("data").split('\n')
        for row in rows:
            row = row.split(',')
            print(row)
            print(User_ieti.objects.filter(email=row[1]).exists())
            if (User_ieti.objects.filter(email=row[1]).exists()):
                if data.get('warning') is None:
                    data['warning'] = True
                    data['warningMsg'] = "Les adreces de correu electrònic següents ja estan registrades:\\n"
                data['warningMsg'] += row[1] + "\\n"
                continue
            try:
                user = User_ieti.objects.create(username=row[0], email=row[1], first_name=row[2], last_name=row[3], role=row[4], date_of_birth=row[5].replace("\r", ""))
                user.save()
            except Exception as e:
                print(e)
                if data.get('error') is None:
                    data['error'] = True
                    data['errorMsg'] = "S'ha produït un error en la importació dels següents usuaris:\\n"
                data['errorMsg'] += row[1] + "\\n"
                continue
        data['info'] = True
        data['infoMsg'] = "Importació finalitzada correctament."
        if data.get('error'):
            data['errorMsg'] += "Si us plau, revisa els camps i torna a intentar-ho."
            #product = Product.objects.create(ISBN=row[0], name=row[1], author=row[2], publication_year=row[3], price=row[4], availability=row[5])
            #product.save()
    return render(request, 'import_csv.html', data)

def add_user(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("name")
        email = request.POST.get("email")
        role = request.POST.get("role")
        cycle = request.POST.get("cycle")
        User_ieti.objects.create(username=username, email=email, role=role, cycle=cycle, password="Password12345erfdsc<vs")
    return render(request, 'add_user.html')

def edit_user_list(request):
    data = {"users": list(User_ieti.objects.all())}
    return render(request, 'edit_user_list.html', data)

def test(request):
    return render(request, 'test.html')
