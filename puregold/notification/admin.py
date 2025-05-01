from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Notification)
class Notifications(admin.ModelAdmin):
    list_display = ('user','title', 'message', 'is_read', 'created_at',)
    search_fields = ('user','title', 'mesage', 'is_read', 'created_at',)