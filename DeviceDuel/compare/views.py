import asyncio
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.urls import reverse
from django.shortcuts import render
from .models import Smart_Phones,Laptops,Smart_Watches
import time


@csrf_exempt
def compare_Page(request):
    SmartPhones = Smart_Phones.objects.all()
    Laptop = Laptops.objects.all()
    SmartWatches = Smart_Watches.objects.all()
    return render(request,"compare.html",{'SmartPhones':SmartPhones ,'Laptops' : Laptop , 'SmartWatches':SmartWatches})
    
def Product_Specification(data):
    SmartPhones = Smart_Phones.objects.all()
    selectedObjs = []
    if list(data.keys())[0] == "SmartPhones":
        ids_list = list(map(int,data["SmartPhones"]))
        for Phone in SmartPhones:
            if Phone.id in ids_list:
                selectedObjs.append(Phone)
    return selectedObjs  

def compare_selected_handler(request):
    if request.method == "POST":
        data = json.loads(request.body)
        key = list(data.keys())[0]
        ids_list = list(map(int,data[key]))
        request.session["key"] = key
        request.session[key] = ids_list
        return JsonResponse({'redirect_url': reverse('Product_Details')})

def Product_Details(request):
    SmartPhones = Smart_Phones.objects.all()
    Product_Detail = []
    mode = request.session.get("key")
    print(f"🍒 Received Mode: {mode}")
    if mode == "SmartPhones":
        selected_ids = request.session.get(mode)
        Product_Detail = Smart_Phones.objects.filter(id__in=selected_ids)
    if mode == "Laptops":
        selected_ids = request.session.get(mode)
        Product_Detail = Laptops.objects.filter(id__in=selected_ids)
    if mode == "SmartWatches":
        selected_ids = request.session.get(mode)
        Product_Detail = Smart_Watches.objects.filter(id__in=selected_ids)
    print(f" 🔔 Received Product Data: {Product_Detail}")
    return render(request,"compare_selected.html",{ "mode" : mode,'SmartPhones':SmartPhones ,'Product_Detail' : Product_Detail })           
# Create your views here.
