from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Data1(models.Model):
    client= models.CharField(max_length=100,default='Hi')
    Answer1= models.CharField(max_length=100,default='Hi')
    Answer2= models.CharField(max_length=200,default='Hi')
    Answer3= models.CharField(max_length=200,default='Hi')
    
class Data2(models.Model):
    client= models.CharField(max_length=100,default='Hi')
    Answer1= models.CharField(max_length=100,default='Hi')
    Answer2= models.CharField(max_length=200,default='Hi')
    Answer3= models.CharField(max_length=200,default='Hi')
    
