from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, PasswordReset
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user','profile_image', 'phone_number','is_verified')
    search_fields = ('phone_number', 'address', 'is_verified')

@admin.register(PasswordReset)
class PasswordReset(admin.ModelAdmin):
    list_display = ('user','reset_id', 'created_when')
    search_fields = ('user', 'reset_id', 'created_when')