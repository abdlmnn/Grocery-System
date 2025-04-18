from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
from .models import *


# Auth
def login(request):
    con = {
        'title': 'Administration',
        'timestamp': datetime.now().timestamp(),
    }
    return render(request,'login.html',con)

def logoutView(request):
    logout(request)
    return redirect('/adminpanel/login/')

def forgotPassword(request):
    context = {
        'title': 'Forgot Password Admin',
        'timestamp': datetime.now().timestamp(),
    }
    return render(request,'forgot-pass/forgot-password.html',context)

def resetPassword(request):
    context = {
        'title': 'Reset Password Admin',
        'timestamp': datetime.now().timestamp(),
    }
    return render(request,'reset-pass/reset-password.html',context)


# Main
def dashboard(request):
    con = {
        'title': 'Dashboard',
        'timestamp': datetime.now().timestamp(),
    }
    return render(request,'master.html',con)