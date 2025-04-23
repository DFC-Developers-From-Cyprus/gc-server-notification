from django.urls import path
from .views import NotificationAPIView, smtp_test_view

urlpatterns = [
    path('', NotificationAPIView.as_view()),
    path('email_test/', smtp_test_view, name='email_test'),
]