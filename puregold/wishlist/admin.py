from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Wishlist)
class Wishlist(admin.ModelAdmin):
    list_display = ('customer','stock',)
    search_fields = ('customer','stock',)