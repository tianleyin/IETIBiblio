"""
URL configuration for ietiBiblio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import api, views
from biblieti.views import *

urlpatterns = [
    path('busqueda/', busqueda, name='busqueda'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/hello/', api.hello, name='hello'),
    path('api/get_products/<str:type>,<str:availability>,<str:name>,<str:author>,<str:ISBN>,<str:publication_year>,<str:artist>,<int:tracks>,<str:director>,<int:duration>,<str:resolution>,<str:manufacturer>,<str:model>', api.get_products, name='get_products'),
    path('send_log/', api.send_log, name='send_log'),
    path('test/', test),
    path('', login_view, name='login'),
    path('forgot_password/', auth_views.PasswordResetView.as_view(), name='forgot_password'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout_custom.html'), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('user_data/', user_data, name='user_data'),
]
