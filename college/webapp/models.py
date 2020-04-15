from django.db import models
import datetime
# Create your models here.

class Notice(models.Model):
    notice = models.CharField(max_length=1000)
    images = models.FileField(upload_to='notice/images/', default='', blank=True, null=True)
    pdf = models.FileField(upload_to='notice/files/',default='', blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.notice


class Feedback(models.Model):
    name = models.CharField(max_length=25)
    feedback = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.feedback

class Student(models.Model):
    name = models.CharField(max_length=25)
    father_name = models.CharField(max_length=25)
    mother_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.email


class Account(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.email

class Admin(models.Model):
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name