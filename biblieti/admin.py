from django.contrib import admin
from .models import *

class LogsAdmin(admin.ModelAdmin):
    list_display = ('date', 'type', 'client_ip', 'action', 'user_mail', 'current_page')
    list_filter = ('date', 'type', 'client_ip', 'user_mail')
    search_fields = ('date', 'action', 'user_mail', 'current_page')
    readonly_fields = ('date', 'type', 'client_ip', 'action', 'user_mail', 'current_page')

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(CD)
admin.site.register(DVD)
admin.site.register(BR)
admin.site.register(Device)
admin.site.register(Logs, LogsAdmin)