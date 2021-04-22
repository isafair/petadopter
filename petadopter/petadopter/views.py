
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('homepage')
    return render(request, 'home.html')


def base(request):
    # return HttpResponse('homepage')
    return render(request, 'base.html')
