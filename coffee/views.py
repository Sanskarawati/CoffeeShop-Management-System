from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee


def home(request):
    coffee = Coffee.objects.all()
    return render(request,'home.html',{'coffee':coffee})

def home1(request):
    return render(request,'home1.html')

def contact(request):
    return render(request,'contact.html')