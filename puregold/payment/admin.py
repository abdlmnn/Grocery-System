from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Payment)
class Payment(admin.ModelAdmin):
    list_display = ('customer','order','method','image', 'status', 'date')
    search_fields = ('customer','order','method','image', 'status', 'date')