from django.db import models

# Create your models here.
class faculty_registration(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phoneno=models.IntegerField(null="True",blank="True")
    batch=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
class studentregistration(models.Model):
    admission_no=models.CharField(max_length=200)
    admission_date=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    dob=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    mobile=models.IntegerField(null="True",blank="True")
    guardian=models.CharField(max_length=200)
    batch=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
class marksubmit(models.Model):
    student_name=models.CharField(max_length=200)
    assess_no=models.CharField(max_length=200)
    max_mark=models.CharField(max_length=200)
    subject_1=models.CharField(max_length=200)
    subject_2=models.CharField(max_length=200)
    subject_3=models.CharField(max_length=200)
    subject_4=models.CharField(max_length=200)
    subject_5=models.CharField(max_length=200)
class attendances(models.Model):
    
    student_name=models.CharField(max_length=200)
    Date=models.CharField(max_length=200)
    status_h1=models.CharField(max_length=200)
    status_h2=models.CharField(max_length=200)
    status_h3=models.CharField(max_length=200)
    status_h4=models.CharField(max_length=200)
    status_h5=models.CharField(max_length=200)
