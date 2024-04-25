from django.contrib import admin
from .models import *

class LogsAdmin(admin.ModelAdmin):
    list_display = ('date', 'type', 'client_ip', 'action', 'current_page')
    list_filter = ('date', 'type', 'client_ip')
    search_fields = ('date', 'action', 'current_page')
    readonly_fields = ('date', 'type', 'client_ip', 'action', 'current_page')

# Register your models here.
admin.site.register(User_ieti)
admin.site.register(Book)
admin.site.register(CD)
admin.site.register(DVD)
admin.site.register(BR)
admin.site.register(Device)
admin.site.register(Logs, LogsAdmin)
admin.site.register(Booking)
admin.site.register(Loan)
admin.site.register(Petition)