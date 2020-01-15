from django.db import models

# Create your models here.
class student_leave(models.Model):
    leave=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    leave_on=models.CharField(max_length=200)
    leave_upto=models.CharField(max_length=200)
    reason=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default='pending')

    
