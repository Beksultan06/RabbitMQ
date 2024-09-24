from django.shortcuts import render
from apps.MQ.models.base import Base

def base(request):
    base = Base.objects.latest('id')
    return render(request, 'index.html', locals())