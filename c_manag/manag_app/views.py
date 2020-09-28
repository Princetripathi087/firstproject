from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import register, detail,requarement
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
import requests
import json
from django.contrib import auth
from django import template
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
#from paytm import Checksum
#from Crypto.Hash import BLAKE2s
#import Crypto
#from Crypto.Hash import SHA
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'
# Create your views here.
def index(request):
    errorLogin = False
    errorEmail = False
    errorPass = False
    errorUser = False
    if 'login' in request.POST:
        un = request.POST['un']
        pas = request.POST['pas']
        user = authenticate(username=un,password=pas)
        if user:
            login(request,user)
            if request.user.is_staff:
                return redirect('details')
            else:
                return render(request,'index.html')
        else:
            errorLogin = True
    if 'Register' in request.POST:
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        ev = json.loads(requests.get('https://api.trumail.io/v2/lookups/json?email='+em).text)
        un = request.POST['un']
        pas1 = request.POST['pas1']
        pas2 = request.POST['pas2']
        check = User.objects.filter(username=em)
        #if (ev['validFormat'] is not True) or (ev['deliverable'] is not True):
           # errorEmail = True
        if pas1 != pas2:
            errorPass = True
        elif check:
            errorUser = True
        else:
            User.objects.create_user(username=em, password=pas1,is_staff = False)
            register.objects.create(f_name=fn,l_name=ln)
            user = authenticate(username =em, password = pas1)
            login(request, user)
            return redirect('index')
        print('values = ',em,pas1,pas2)
    d= {'errorPass':errorPass,'errorEmail':errorEmail,'errorL':errorLogin}
    return render(request,'index.html',d)
    
def details(request):
    
        #if request.user.is_authenticated:
           # return redirect('details')
        if 'details' in request.POST:
            name = request.POST['name']
            email = request.POST['email']
            con = request.POST['con']
            gen = request.POST['gen']
            add = request.POST['add']
            o=detail.objects.create(user = request.user,c_name=name,c_email=email,c_cont=con,gender=gen,add=add)
            o.save()
            return redirect('requarement')
                
        return render(request,'details.html')
            #return render(request,'details.html')    

def requarements(request):
    if 'requarement' in request.POST:
        typeofveg = request.POST.get('typeofveg')
        numpack = request.POST['numpack']
        datesub = request.POST['datesub']
        deldate = request.POST['deldate']
        amount = request.POST['amount']
        lorrytype = request.POST.get('lorrytype')
        lorrynumber = request.POST['lorrynumber']
        drivnum = request.POST['drivnum']
        requarement.objects.create(vegTyp=typeofveg,numPack=numpack,sumitD=datesub,deliD=deldate,amount=amount,lorryType=lorrytype,lorryNum=lorrynumber,drivName=drivnum)
        #return redirect('submit')
    #if 'submit' in request.POST:
        sub = "conform"
        from_mail = settings.EMAIL_HOST_USER
        data = dict()
        data = {'name':detail.c_name,'datesub':requarement.sumitD,'deldate':requarement.deliD}
        html = get_template('mail.html').render(data)
        msg = EmailMultiAlternatives(sub,'',from_mail)
        msg.attach_alternative(html, 'text/html')
        print('result=', msg.send())
        return redirect('submit')
    return render(request,'requarement.html')



def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def submit(request):
    return render(request,'submit.html')

#def Home(request):
  #  return render(request,'index.html')

'''def Test(request):
    detail.objects.create(c_name='abc',c_email='xyz', c_cont='exapmle@gmail.com',gender='123', add='123')
    return redirect('')'''