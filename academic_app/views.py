from django.shortcuts import render
from academic_app.models import faculty_registration,studentregistration,marksubmit,attendances
from studentapp.models import student_leave
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request,'index.html')
def faclogin(request):
    return render(request,'login.html')
def facloginsubmit(request):
    if request.method=='POST':
        username=request.POST.get('staffAccount')
        password=request.POST.get('staffPassword')
        username=str(username)
        password=str(password)
        request.session['usr']=username
        u=studentregistration.objects.filter(name=username)
        v=studentregistration.objects.filter(password=password)
        if u.count()==1 and v.count()==1:
            return render(request,'home.php')
        else:
            a=faculty_registration.objects.filter(username=username)
            b=faculty_registration.objects.filter(password=password)
            if a.count()==1 and b.count()==1:
                return render(request,'faculty-login.html')
        
def facprofile(request):
    queryset=faculty_registration.objects.all().filter(username=request.session['usr'])
    return render(request,'faculty-profile.html',{'key':queryset})  
def studentleavephp(request):
    queryset = student_leave.objects.all()
    return render(request,'student-leave.php',{'authors':queryset})  
def leaveapproval(request):
    if request.method=='POST': 
        leave=request.POST.get('leave')
        
        student_leave.objects.filter(leave=leave).update(status='Approved')
    queryset = student_leave.objects.all()
    return render(request,'student-leave.php',{'authors':queryset})  
def assessment_php(request):
    return render(request,'assessment.php')
def Marksubmit(request):
    if request.method=='POST': 
        student_name=request.POST.get('student_name')
        assess_no=request.POST.get('assess_no')
        max_mark=request.POST.get('max_mark')
        subject_1=request.POST.get('subject_1')
        subject_2=request.POST.get('subject_2')
        subject_3=request.POST.get('subject_3')
        subject_4=request.POST.get('subject_4')
        subject_5=request.POST.get('subject_5')
        a=marksubmit(student_name=student_name,assess_no=assess_no,max_mark=max_mark, subject_1= subject_1, subject_2= subject_2,subject_3= subject_3,subject_4= subject_4, subject_5= subject_5)
        a.save()
        return render(request,'assessment.php')
def attendence_1_php(request):
    return render(request,'attendence_1.php')
def Attendancesubmit(request):
    
    if request.method=='POST':

        student_name=request.POST.get('student_name')
        date=request.POST.get('date')
        name=request.POST.get('name')
        status_h1=request.POST.get('status_h1')
        status_h2=request.POST.get('status_h2')
        status_h3=request.POST.get('status_h3')
        status_h4=request.POST.get('status_h4')
        status_h5=request.POST.get('status_h5')
        a=attendances(student_name=student_name,Date=date,status_h1=status_h1,status_h2=status_h2,status_h3=status_h3,status_h4=status_h4,status_h5=status_h5)
        a.save()
    return render(request,'attendence_1.php')
def faculty_profile_edit_php(request):
    queryset=faculty_registration.objects.all().filter(username=request.session['usr'])
    return render(request,'faculty-profile-edit.php',{'key':queryset})
def faceditprofile(request):
    if request.method=='POST': 
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        batch=request.POST.get('batch')
        faculty_registration.objects.filter(name=request.session['usr']).update(name=name,email=email,phoneno=phoneno,batch=batch)
    queryset=faculty_registration.objects.all().filter(username=request.session['usr'])
    return render(request,'faculty-profile-edit.php',{'key':queryset})
def logouts(request):
    django_logout(request)
    return render(request,'login.html')    
    