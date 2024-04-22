from django.http import JsonResponse
from .models import *

from rest_framework.decorators import api_view
# from rest_framework.decorators import api_view

def hello(request):
    # jsonData = list( Producte.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "hello": "World",
        }, safe=False)

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