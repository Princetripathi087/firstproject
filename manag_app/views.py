from django.shortcuts import render
from django import template
# Create your views here.
def index(request):
    return render(request,'index.html')
def details(request):
    return render(request,'details.html')

def requarement(request):
    return render(request,'requarement.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')