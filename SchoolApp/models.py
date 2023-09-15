from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length = 150)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()
    created_at=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    rollnumber=models.IntegerField(unique=True)
    name=models.CharField(max_length=25,blank=False,null=False,unique=True)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=25,blank=False,null=False)
    def __str__(self):
        return self.name
class StudentFamily(models.Model):
    name=models.ForeignKey(Student,on_delete=models.CASCADE)
    #rollnumber=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='topic_content_type',default=None)
    father_name=models.CharField(max_length=20)
    mother_name=models.CharField(max_length=30)
    emergency=models.CharField(max_length=10,unique=True)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.father_name