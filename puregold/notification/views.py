from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    return render(request, 'notification.html', {'title': 'Notifications', 'notifications': notifications})

def read_all(request):
    if request.user.is_superuser:
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return redirect(request.META.get('HTTP_REFERER', 'adminpanel:dashboard'))
    else: 
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return redirect(request.META.get('HTTP_REFERER', 'notification:notifications'))

def clear_all(request):
    if request.user.is_superuser:
        Notification.objects.filter(user=request.user, is_read=False).delete()
        return redirect(request.META.get('HTTP_REFERER', 'adminpanel:dashboard'))
    else: 
        Notification.objects.filter(user=request.user, is_read=False).delete()
        return redirect(request.META.get('HTTP_REFERER', 'notification:notifications'))
    
def read(request, id):
    if request.user.is_superuser:
        notif = get_object_or_404(Notification, id=id)
        notif.is_read = True
        notif.save()
        return redirect(request.META.get('HTTP_REFERER', 'adminpanel:dashboard'))
    else: 
        notif = get_object_or_404(Notification, id=id)
        notif.is_read = True
        notif.save()
        return redirect(request.META.get('HTTP_REFERER', 'notification:notifications'))

def delete(request, id):
    if request.user.is_superuser:
        notif = get_object_or_404(Notification, id=id)
        notif.delete()
        return redirect(request.META.get('HTTP_REFERER', 'adminpanel:dashboard'))
    else: 
        notif = get_object_or_404(Notification, id=id)
        notif.delete()
        return redirect(request.META.get('HTTP_REFERER', 'notification:notifications'))