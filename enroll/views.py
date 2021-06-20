from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

# This Function will Add new Item and Show All Items
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['Name']
            em = fm.cleaned_data['Email']
            pd = fm.cleaned_data['Password']
    
            reg = User(Name=nm, Email=em, Password=pd)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form': fm,'stu':stud})


# This Function will Update/Edit the Item

def Update_Data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)  
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudents.html', {'form': fm})

# This Function will Delete Item from Table

def Delete_Data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
         
