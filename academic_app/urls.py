from django.contrib import admin
from academic_app import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('login.php',views.faclogin,name='login'),
    path('faculty-login.php',views.facloginsubmit,name='facloginsubmit'),
    path('faculty-login',views.facprofile,name='facprofile'),
    path('student-leave.php',views.studentleavephp,name='student-leavephp'),
    path('leaveapproval',views.leaveapproval,name='leaveapproval'),
    path('assessment_php',views.assessment_php,name='assessment_php'),
    path('marksubmit',views.Marksubmit,name='marksubmit'),
    path('attendence_1_php',views.attendence_1_php,name='attendence_1_php'),
    path('Attendancesubmit',views.Attendancesubmit,name="Attendancesubmit"),
    path('faculty_profile_edit_php',views.faculty_profile_edit_php,name="faculty_profile_edit_php"),
    path('faceditprofile',views.faceditprofile,name="faceditprofile"),
    path('index.php',views.logouts,name="logouts"),








     
]