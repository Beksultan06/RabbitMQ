from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)
    return f"Email sent to {', '.join(recipient_list)}"
