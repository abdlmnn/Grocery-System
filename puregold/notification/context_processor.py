from .models import Notification

def notifications_processor(request):
    if request.user.is_authenticated:
        notifications_qs = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
        notifications = notifications_qs[:10]
        unread_count = notifications_qs.filter(is_read=False).count()
    else:
        notifications = []
        unread_count = 0
    return {
        'notifications': notifications,
        'unread_count': unread_count,
    }