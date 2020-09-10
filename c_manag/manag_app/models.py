from django.db import models
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
    c_name = models.CharField(max_length=30)
    c_email = models.EmailField()
    c_cont = models.IntegerField()
    gender = models.CharField(max_length=50,null=True)
    add = models.CharField(max_length=50)
    def __str__(self):
        return self.c_name
