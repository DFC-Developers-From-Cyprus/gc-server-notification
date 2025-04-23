from django.http import HttpResponse

# Email
from .utils import send_email

# API
from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer


# View to check that REST works
class NotificationAPIView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


# View to check that SMTP works
def smtp_test_view(request):
    send_email(
        subject="SMTP Works!",
        message="This is the test mail.",
        to_email="kirill.dorokh@gmail.com"
    )
    return HttpResponse("Email has been sent")




