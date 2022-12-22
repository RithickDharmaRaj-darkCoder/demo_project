
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import students_data

# Create your views here.

def home(request):
    mydata = students_data.objects.all()
    if mydata != '':
        return render(request, "home.html",{'mydata':mydata})
    else:
        return render(request, "home.html")

def addData(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        age = request.POST.get('age', False)
        address = request.POST.get('address', False)
        contact = request.POST.get('contact', False)
        mail = request.POST.get('mail', False)
        
        std_data = students_data()
        std_data.Name = name
        std_data.Age = age
        std_data.Address = address
        std_data.Contact = contact
        std_data.Mail = mail
        std_data.save()
        return redirect('home')
        
    return render(request, "home.html")

def updateData(request, id):
    mydata = students_data.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name', False)
        age = request.POST.get('age', False)
        address = request.POST.get('address', False)
        contact = request.POST.get('contact', False)
        mail = request.POST.get('mail', False)
        
        mydata.Name = name
        mydata.Age = age
        mydata.Address = address
        mydata.Contact = contact
        mydata.Mail = mail
        mydata.save()
        return redirect('home')
    return render(request, "update.html", {'data':mydata})


def deleteData(request, id):
    mydata = students_data.objects.get(id=id)
    mydata.delete()
    return redirect('home')

