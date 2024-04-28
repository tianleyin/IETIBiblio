from django.http import JsonResponse
from .models import *
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import timedelta
import json
# from rest_framework.decorators import api_view

def hello(request):
    # jsonData = list( Producte.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "hello": "World",
        }, safe=False)

@api_view(['GET'])
def get_products_landing(request, search):
    try:
        search_int = int(search)
    except ValueError:
        search_int = 99999999999999999999999999999999999999999999999999999999

    filteredData = Catalogue.objects.filter(

        Q(name__icontains=search) |  # Usamos icontains para que la búsqueda no sea sensible a mayúsculas y minúsculas
        Q(book__author__icontains=search) |
        Q(book__ISBN__icontains=search) |
        Q(book__publication_year__icontains=search_int) |
        Q(cd__artist__icontains=search) |
        Q(cd__tracks__contains=search_int) |
        Q(dvd__director__icontains=search) |
        Q(dvd__duration__contains=search_int) |
        Q(br__resolution__icontains=search) |
        Q(device__manufacturer__icontains=search) |
        Q(device__model__icontains=search)

    ).distinct()

    #return JsonResponse(list(filteredData.values()), safe=False)
    # Serializa los resultados y devuelve una respuesta JSON
    serialized_data = [item.serialize() for item in filteredData]
    return JsonResponse(serialized_data, safe=False)

@api_view(['GET'])
def get_products(request, type, availability, name, author, ISBN, publication_year, artist, tracks, director, duration, resolution, manufacturer, model):
    print(type)
    if (name == 'null'):
        name = ''
    if (author == 'null'):
        author = ''
    if (ISBN == 'null'):
        ISBN = ''
    if (artist == 'null'):
        artist = ''
    if (director == 'null'):
        director = ''
    if (resolution == 'null'):
        resolution = ''
    if (manufacturer == 'null'):
        manufacturer = ''
    if (model == 'null'):
        model = ''
    filteredData = []
    if (type == 'Any'):
        if (publication_year != 'null'):
            bookData = list(Book.objects.filter(name__contains=name,author__contains=author,ISBN__contains=ISBN,publication_year=publication_year).values())
        else:
            bookData = list(Book.objects.filter(name__contains=name,author__contains=author,ISBN__contains=ISBN).values())
        for item in bookData:
            item['type'] = 'Book'
        filteredData.extend(bookData)
        if (tracks != 0):
            cdData = list(CD.objects.filter(name__contains=name,artist__contains=artist,tracks=tracks).values())
        else:
            cdData = list(CD.objects.filter(name__contains=name,artist__contains=artist).values())
        for item in cdData:
            item['type'] = 'CD'
        filteredData.extend(cdData)
        if duration != 0:
            dvdData = list(DVD.objects.filter(name__contains=name,director__contains=director,duration=duration).values())
        else:
            dvdData = list(DVD.objects.filter(name__contains=name,director__contains=director).values())            
        for item in dvdData:
            item['type'] = 'DVD'
        filteredData.extend(dvdData)
        brData = list(BR.objects.filter(name__contains=name,resolution__contains=resolution).values())
        for item in brData:
            item['type'] = 'BR'
        filteredData.extend(brData)
        deviceData = list(Device.objects.filter(name__contains=name,manufacturer__contains=manufacturer,model__contains=model).values())
        for item in deviceData:
            item['type'] = 'Device'
        print(filteredData)
        filteredData.extend(deviceData)
    elif (type == 'Book'):
        if (publication_year != 'null'):
            filteredData = list(Book.objects.filter(name__contains=name,author__contains=author,ISBN__contains=ISBN,publication_year=publication_year).values())
        else:
            filteredData = list(Book.objects.filter(name__contains=name,author__contains=author,ISBN__contains=ISBN).values())
        for item in filteredData:
            item['type'] = 'Book'
    elif (type == 'CD'):
        if (tracks != 0):
            filteredData = list(CD.objects.filter(name__contains=name,artist__contains=artist,tracks=tracks).values())
        else:
            filteredData = list(CD.objects.filter(name__contains=name,artist__contains=artist).values())
        for item in filteredData:
            item['type'] = 'CD'
    elif (type == 'DVD'):
        if duration != 0:
            filteredData = list(DVD.objects.filter(name__contains=name,director__contains=director,duration=duration).values())
        else:
            filteredData = list(DVD.objects.filter(name__contains=name,director__contains=director).values())
        for item in filteredData:
            item['type'] = 'DVD'
    elif (type == 'BR'):
        filteredData = list(BR.objects.filter(name__contains=name,resolution__contains=resolution).values())
        for item in filteredData:
            item['type'] = 'BR'
    elif (type == 'Device'):
        filteredData = list(Device.objects.filter(name__contains=name,manufacturer__contains=manufacturer,model__contains=model).values())
        for item in filteredData:
            item['type'] = 'Device'
    for item in filteredData:
        if Booking.objects.filter(catalogue_id=item['id']).exists():
            if availability == 'available':
                filteredData.remove(item)
            else:
                item['available'] = False
        else:
            if availability == 'not-available':
                filteredData.remove(item)
            else:
                item['available'] = True
    return JsonResponse(filteredData, safe=False)

@api_view(['POST'])
def send_log(request):
    try:
        data = request.data
        current_date = timezone.now()
        level = data.get('type')
        client_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('HTTP_CLIENT_IP') or request.META.get('REMOTE_ADDR')
        action = data.get('message')
        current_page = data.get('current_page')
        
        if current_date and level and client_ip and action and current_page:
            log_entry = Logs.objects.create(date=current_date, type=level, client_ip=client_ip, action=action, current_page=current_page)
            log_entry.save()
            return Response({'success': True})
        else:
            return Response({'success': False, 'error': 'Datos incompletos', 'current_date':current_date, 'level':level, 'client_ip':client_ip, 'action':action, 'current_page':current_page})

    except Exception as e:
        # Captura cualquier excepción y envía los detalles como respuesta
        return Response({'success': False, 'error': str(e)})
    
@api_view(['POST'])
def do_loan(request):
    if request.method == 'POST':
        data = {}
        # Obtener el correo electrónico del cuerpo de la solicitud POST
        email = request.data.get('email')
        # Obtener el id del Catálogo
        catalogue_id = request.data.get('id')

        # Comprobar si existe un usuario con ese correo electrónico
        try:
            user = User_ieti.objects.get(email=email)
            catalogue = Catalogue.objects.get(id=catalogue_id)

            loan = Loan.objects.create(
                catalogue=catalogue,
                user=user,
                date_of_loan=timezone.now(),
                date_of_return=timezone.now() + timedelta(days=30)  # La fecha de retorno se puede establecer más tarde con un archivo de configuracion o por un campo en el formulario de loan_form
            )

            # Guardar el préstamo en la base de datos
            loan.save()
            #data['info'] = True
            #data['infoMsg'] = 'Préstec realitzat correctament'

            messages.success(request, 'Préstec realitzat correctament')
            return redirect("loans")

        except User_ieti.DoesNotExist:
            # Si el usuario no existe, hacer algo aquí
            data['error'] = True
            data['errorMsg'] = 'Usuari amb correu ' + email + ' no trobat'
            return render(request, 'loans_form.html', data)
        
        except Catalogue.DoesNotExist:
            data['error'] = True
            data['errorMsg'] = 'Element no disponible per prestar. No existeix'
            return render(request, 'loans_form.html', data)
        
        except Exception as e:
            print(e)
            data['error'] = True
            data['errorMsg'] = 'Error al realitzar el préstec.'
            return render(request, 'loans_form.html', data)
        