from django.shortcuts import render,redirect
from django.contrib import messages
from .models import UserRegistration

def Contact(request):
    if request.method == "POST":
        firstName = request.POST.get("First_Name")
        lastName = request.POST.get("Last_Name")
        email = request.POST.get("Email")
        number = request.POST.get("Number")
        feedback = request.POST.get("Feedback")
        gender = request.POST.get("gender")
        data = UserRegistration(firstName = firstName, lastName = lastName, email = email ,number = number, feedback = feedback, gender = gender)
        messages.success(request,"Feedback submitted successfully!")
        data.save()
        return redirect(request.path)
    return render(request,'contact.html')

def About(request):
    return render(request,'about.html')
# Create your views here.
