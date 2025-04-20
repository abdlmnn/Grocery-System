from django.urls import path
from .views import *

urlpatterns = [
    # Auth
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('forgot-password/',forgotPassword,name='forgotPassword'),
    path('sent-reset-password/<str:reset_id>/',sentResetPassword,name='sent-reset-password'),
    path('reset-password/<str:reset_id>/',resetPassword,name='reset-password'),
    
    # Main
    path('',dashboard,name='dashboard'),
] 
