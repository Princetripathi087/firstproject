from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import register, detail
from django.contrib.auth import login,logout,authenticate
import requests
import json
from django.contrib import auth
from django import template
# Create your views here.
def index(request):
    errorEmail = False
    errorPass = False
    if request.method == 'POST':
        U = auth.authenticate(ea=request.POST['ea'],pas=request.POST['pas'])
        if U is not None:
            auth.login(request,U)
            return redirect('details')
        else:
            return render(request,'index.html',{'error':'Email or Password is incorrect'})
    else:
        return render(request,'index.html')
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
    
def details(request):
    if 'details' in request.POST:
        if request.user.is_authenticated:
            print("2")
            return redirect('details')
        
        name = request.POST['name']
        email = request.POST['email']
        print(email)
        con = request.POST['con']
        gen = request.POST['gen']
        add = request.POST['add']
        o=detail.objects.create(c_name=name,c_email=email,c_cont=con,gender=gen,add=add)
        o.save()
        print("1")
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
    detail.objects.create(c_name='abc',c_email='xyz', c_cont='exapmle@gmail.com',gender='123', add='123')
    return redirect('')'''