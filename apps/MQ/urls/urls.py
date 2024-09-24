from django.urls import path
from apps.MQ.views.base import base
from apps.MQ.views.contact import contact

urlpatterns = [
    path('', base, name='base'),
    path('contact', contact, name='contact')
]
