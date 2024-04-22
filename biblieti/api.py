from django.http import JsonResponse
from .models import *
from django.utils import timezone
from rest_framework.decorators import api_view
import json
# from rest_framework.decorators import api_view

def hello(request):
    # jsonData = list( Producte.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "hello": "World",
        }, safe=False)

@api_view(['GET'])
def get_products(request, type, availability):
    filteredData = []
    if (type == 'Any'):
        bookData = list(Book.objects.all().values())
        filteredData.extend(bookData)
        cdData = list(CD.objects.all().values())
        filteredData.extend(cdData)
        dvdData = list(DVD.objects.all().values())
        filteredData.extend(dvdData)
        brData = list(BR.objects.all().values())
        filteredData.extend(brData)
        deviceData = list(Device.objects.all().values())
        filteredData.extend(deviceData)
    elif (type == 'Book'):
        filteredData = list(Book.objects.filter(name__contains=availability).values())
    elif (type == 'CD'):
        filteredData = list(CD.objects.all().values())
    elif (type == 'DVD'):
        filteredData = list(DVD.objects.all().values())
    elif (type == 'BR'):
        filteredData = list(BR.objects.all().values())
    elif (type == 'Device'):
        filteredData = list(Device.objects.all().values())
    for item in filteredData:
        if Booking.objects.filter(catalogue_id=item['id']).exists():
            if request.data.get('availability' == 'available'):
                filteredData.remove(item)
            else:
                item['available'] = False
        else:
            if request.data.get('availability' == 'not-available'):
                filteredData.remove(item)
            else:
                item['available'] = True
    return JsonResponse(filteredData, safe=False)


@api_view(['POST'])
def send_log(request):
    data = json.loads(request.body)
    current_date = timezone.now()
    level = data.get('type')
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('HTTP_CLIENT_IP') or request.META.get('REMOTE_ADDR')
    action = data.get('message')
    user_mail = data.get('user_mail')
    current_page = request.META.get('HTTP_REFERER')
    
    if current_date and level and client_ip and action and user_mail and current_page:
        log_entry = Logs.objects.create(date=current_date, type=level, client_ip=client_ip, action=action, user_mail=user_mail, current_page=current_page)
        log_entry.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Datos incompletos'})