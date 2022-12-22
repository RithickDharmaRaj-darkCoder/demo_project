
from django.shortcuts import render
from django.http import HttpResponse
from .models import students_data

# Create your views here.

def home(request):
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
        
    return render(request, "home.html")




