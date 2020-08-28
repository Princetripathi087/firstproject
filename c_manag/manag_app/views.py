from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import register
from django.contrib.auth import login,logout,authenticate
import requests
import json
from django import template
# Create your views here.
def index(request):
    errorEmail = False
    errorPass = False
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        ev = json.loads(requests.get('https://api.trumail.io/v2/lookups/json?email='+em).text)
        pas1 = request.POST['pas1']
        pas2 = request.POST['pas2']
        if (ev['validFormat'] is not True) or (ev['deliverable'] is not True):
            errorEmail = True
        if pas1 != pas2:
            errorPass = True
        obj=register.objects.create(f_name = fn,l_name = ln, email =em, passw=pas1, repassw=pas2)
        obj.save()
        return redirect('index')
    d= {'errorPass':errorPass,'errorEmail':errorEmail}
    return render(request,'index.html',d)
    
    if request.method == 'POST':
            ea = request.POST['ea']
            pas = request.POST['pas']
            register.authenticate(email=ea,passw=pas)
            if not register.is_staff:
                login(request,register)
                return redirect('index')
    return render(request,'details.html')        
    
    
def details(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        con = request.POST['con']
        gen = request.POST['gen']
        add = request.POST['add']
        o=detail.objects.create(c_name=name,c_email=email,c_cont=con,gender=gen,add=add)
        o.save()
        return render(request,'details.html')
    return render(request,'details.html')

def requarement(request):
    return render(request,'requarement.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def payment(request):
    return render(request,'payment.html')

'''def Test(request):
    register.objects.create(f_name='abc',l_name='xyz', email='exapmle@gmail.com',passw='123', repassw='123')
    return redirect('index')'''