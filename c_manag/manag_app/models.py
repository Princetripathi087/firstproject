from django.db import models
from django.contrib.auth.models import User
from django import forms

class register(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField()
    passw = models.CharField(max_length=10)
    repassw = models.CharField(max_length=10)
    def __str__(self):
        return self.f_name

class login(models.Model):
    l_email = models.EmailField()
    passw = models.CharField(max_length=10)
    def __str__(self):
        return self.l_email

class detail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    c_name = models.CharField(max_length=30)
    c_email = models.EmailField()
    c_cont = models.IntegerField()
    gender = models.CharField(max_length=50,null=True)
    add = models.CharField(max_length=50)
    def __str__(self):
        return self.c_name

class requarement(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    vegTyp = models.CharField(max_length=50,null=True)
    numPack = models.IntegerField()
    sumitD = models.DateField()
    deliD = models.DateField()
    amount = models.IntegerField(default=0)
    lorryType = models.CharField(max_length=30,null=True)
    lorryNum = models.CharField(max_length=30,null=True)
    drivName = models.CharField(max_length=60,null=True)

