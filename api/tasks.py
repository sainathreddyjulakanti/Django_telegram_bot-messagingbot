from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_email_task(subject, message, user_email):
    return send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL, 
        [user_email],
        fail_silently=False
    )
