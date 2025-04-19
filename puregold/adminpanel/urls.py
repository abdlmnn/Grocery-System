from django.urls import path
from .views import (
    login,
    logout,
    forgotPassword,
    resetPassword,
    dashboard,
)

urlpatterns = [
    # Auth
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('forgot-password/',forgotPassword,name='forgotPassword'),
    path('reset-password/',resetPassword,name='resetPassword'),
    
    # Main
    path('',dashboard,name='dashboard'),
] 
