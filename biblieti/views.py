from django.shortcuts import render

# Create your views here.
def busqueda(request):
    return render(request, 'search_product.html')