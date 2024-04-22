# urls.py
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', user_login, name='login'),
    # Otras URLs aquí
]
