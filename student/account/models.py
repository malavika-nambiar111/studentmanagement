from django.db import models

# Create your models here.

class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phno = models.CharField(max_length=10)

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password=models.CharField(max_length=15)
    phno = models.CharField(max_length=10)