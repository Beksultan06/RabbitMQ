from django.shortcuts import render
from apps.MQ.models.contact import Contact
from apps.MQ.views.rabbit_mq import send_email

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        send_email.delay(subject, message, 'from@example.com', [email])

    return render(request, 'contact.html')
