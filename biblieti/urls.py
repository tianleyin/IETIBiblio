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
    path('loans/', loans, name='loans'),
    path('loans_form/', loans_form, name='loans_form'),
    path('api/do_loan/', api.do_loan, name='do_loan'),
    path('return_loan/', return_loan, name='return_loan'),
    path('api/get_user_loans/', api.get_user_loans, name='get_user_loans'),
    path('api/delete_loan/', api.delete_loan, name='delete_loan'),
    path('api/hello/', api.hello, name='hello'),
    path('api/get_products/<str:type>,<str:availability>,<str:name>,<str:author>,<str:ISBN>,<str:publication_year>,<str:artist>,<int:tracks>,<str:director>,<int:duration>,<str:resolution>,<str:manufacturer>,<str:model>,<int:page>', api.get_products, name='get_products'),
    path('api/get_products_landing/<str:search>,<str:availability>', api.get_products_landing, name='get_products_landing'),
    path('api/send_log/', api.send_log),
    path('test/', test),
    path('', login_view, name='login'),
    path('forgot_password/', auth_views.PasswordResetView.as_view(), name='forgot_password'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('login')), name="password_reset_confirm"),
    #path('reset/', auth_views.SetPasswordForm.as_view(success_url=reverse_lazy('login')), name='set-password'),
   # path('password_reset_confirm <uidb64> <token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout_custom.html'), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('dashboard')), name='change_password'),
    path('user_data/', user_data, name='user_data'),
    path('import_csv/', import_csv, name='import_csv'),
    path('loan_form/', loans_form, name='loans_form'),
    path('add_user', add_user, name='add_user'),
    path('edit_user', edit_user_list, name='edit_user_list'),
    path('edit_user/<str:email>', edit_user_form, name='edit_user_form'),
    path('accounts/', include('allauth.urls')), 
    path('add_product/', add_product_view, name='add_product_view'),
    path('api/search_book_isbn/<str:isbn>', api.search_book_isbn, name='search_book_isbn'),
    path('api/add_product/', api.add_product, name='add_product')

]
