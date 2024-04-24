# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User_ieti(AbstractUser):
    role_choices = [
        ('student', 'Student'),
        ('librarian', 'Librarian'),
        ('superadmin', 'Super Admin')
    ]

    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=40, unique=True)
    #mail = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=role_choices)
    date_of_birth = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=100, null=True, blank=True)
    cycle = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='imgs/', blank=True, null=True)
    USERNAME_FIELD = 'username'
    # def save(self, *args, **kwargs):
    #     # Hashear la contraseña antes de guardarla en la base de datos
    #     if self.password:
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)



class Catalogue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='imgs/', blank=True, null=True)
    def __str__(self):
        return self.name

class Book(Catalogue):
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    publication_year = models.IntegerField()

class CD(Catalogue):
    artist = models.CharField(max_length=100)
    tracks = models.IntegerField()

class DVD(Catalogue):
    director = models.CharField(max_length=100)
    duration = models.IntegerField()

class BR(Catalogue):
    resolution = models.CharField(max_length=100)

class Device(Catalogue):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    user = models.ForeignKey(User_ieti, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    user = models.ForeignKey(User_ieti, on_delete=models.CASCADE)
    date_of_loan = models.DateTimeField()
    date_of_return = models.DateTimeField()

class Petition(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    commentary = models.TextField()
    user = models.ForeignKey(User_ieti, on_delete=models.CASCADE)

class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    type_choices = [
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('fatal', 'Fatal')
    ]
    type = models.CharField(max_length=20, choices=type_choices)
    client_ip = models.CharField(max_length=255)
    action = models.TextField()
    user_name = models.CharField(max_length=255)
    current_page = models.CharField(max_length=255)
    
    def clean(self):
        if self.type not in dict(self.type_choices).keys():
            raise ValidationError('El tipo de log no es válido.')
