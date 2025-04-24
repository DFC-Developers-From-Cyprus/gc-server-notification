from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_task(subject, message, to_email, from_email=None):
    from_email = from_email or settings.DEFAULT_FROM_EMAIL
    return send_mail(subject, message, from_email, [to_email])
