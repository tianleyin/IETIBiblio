from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(CD)
admin.site.register(DVD)
admin.site.register(BR)
admin.site.register(Device)