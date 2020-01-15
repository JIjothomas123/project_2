from django.contrib import admin
from .models import  faculty_registration,studentregistration

# Register your models here.
admin.site.register(faculty_registration)
admin.site.register(studentregistration)

