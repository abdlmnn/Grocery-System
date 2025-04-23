from datetime import datetime

def current_datetime_timestamp(request):
    return {
        'datetime': datetime.now(),
        'timestamp': datetime.now().timestamp(),
    }