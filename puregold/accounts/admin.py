from django.contrib import admin
from .models import Customer

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'lastname', 'is_verified')
    search_fields = ('firstname', 'lastname', 'user__email')