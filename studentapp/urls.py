from django.contrib import admin
from studentapp import views
from django.urls import path

urlpatterns = [
       path('studentlogin',views.stulogin,name='stulogin'),
       path('studentleave',views.studentleave,name='studentleave'),
       path('stuleaveapp',views.stuleaveapp,name='stuleaveapp'),
       path('student_assessment_php',views.student_assessment_php,name='student_assessment_php'),
       path('student_attendence_php',views.student_attendence_php,name='student_attendence_php'),
       path('student_profile_php',views.student_profile_php,name='student_profile_php'),
       path('student_edit_php',views.student_edit_php,name='student_edit_php'),
       path('editprofile',views.editprofile,name='editprofile'),









     
]