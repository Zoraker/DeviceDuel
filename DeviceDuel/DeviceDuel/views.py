from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def home(request):
    print("✅ DEBUG: Home view is being executed!") 
    return render(request,"websites/home.html")
