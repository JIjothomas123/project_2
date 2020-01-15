from django.shortcuts import render
from studentapp.models import student_leave
from academic_app.views import Marksubmit,facloginsubmit
from academic_app.models import marksubmit,attendances,studentregistration


# Create your views here.
def stulogin(request):
    return render(request,'login.html')
def studentleave(request):
    queryset = student_leave.objects.all()
    return render(request,'student-leave-management.php',{'authors':queryset})
def stuleaveapp(request):
    if request.method=='POST':
        leave=request.POST.get('leave')
        name=request.POST.get('name')
        leave_on=request.POST.get('leave_on')
        leave_upto=request.POST.get('leave_upto')
        reason=request.POST.get('reason')
        message=request.POST.get('message')
        a=student_leave(leave=leave,name=name,leave_on=leave_on,leave_upto=leave_upto,reason=reason,message=message)
        a.save()
    queryset = student_leave.objects.all()
    return render(request,'student-leave-management.php',{'authors':queryset})

def student_assessment_php(request):
    query = marksubmit.objects.all().filter(student_name=request.session['usr'])
    return render(request,'student-assessment.php',{'authors':query})
def student_attendence_php(request):
    y = attendances.objects.all().filter(student_name=request.session['usr'])
    return render(request,'student-attendence.php',{'authors':y})
def student_profile_php(request):
    queryset=studentregistration.objects.all().filter(name=request.session['usr'])
    return render(request,'student-profile.php',{'key':queryset})  
def student_edit_php(request):
    queryset=studentregistration.objects.all().filter(name=request.session['usr'])
    return render(request,'student-edit.php',{'key':queryset})  
def editprofile(request):
    if request.method=='POST': 
        admission_no=request.POST.get('admission_no')
        admission_date=request.POST.get('admission_date')
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        guardian=request.POST.get('guardian')
        studentregistration.objects.filter(name=request.session['usr']).update(admission_no=admission_no,admission_date=admission_date,name=name,dob=dob,gender=gender,guardian=guardian,mobile=mobile)
    queryset=studentregistration.objects.all().filter(name=request.session['usr'])
    return render(request,'student-profile.php',{'key':queryset}) 