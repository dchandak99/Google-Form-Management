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

class QuesType(models.Model):
    TypeID= models.IntegerField()
    Type= models.CharField(max_length=50,default='Hi')

class UserForm(models.Model):
    UserID= models.IntegerField()
    FormID= models.IntegerField()
    FormName=models.CharField(max_length=100,default='Hi')

    class Meta:
    	
    	unique_together=(("UserID","FormID"),)

class Question(models.Model):
    QuesID= models.IntegerField()
    FormID= models.ForeignKey(UserForm,on_delete=models.CASCADE)
    TypeID= models.IntegerField()
    Questxt= models.CharField(max_length=100,default='Hi')

    class Meta:
    	unique_together=(("QuesID","FormID"),)


class Mcq(models.Model):
	QuesID= models.ForeignKey(Question,on_delete=models.CASCADE)
	Options= models.CharField(max_length=100,default='Hi')


# type=QuesType(TypeID=1,Type='single line')
# type.save()
# type=QuesType(TypeID=2,Type='paragraph')
# type.save()
# type=QuesType(TypeID=3,Type='single-correct')
# type.save()
# type=QuesType(TypeID=4,Type='multi-correct')
# type.save()
# type=QuesType(TypeID=5,Type='drop-down')
# type.save()
# type=QuesType(TypeID=6,Type='file-upload')
# type.save()
# type=QuesType(TypeID=7,Type='toggle')
# type.save()
# type=QuesType(TypeID=8,Type='rating-scale')









    
    
