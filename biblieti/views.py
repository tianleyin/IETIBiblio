from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def busqueda(request):
    return render(request, 'search_product.html')