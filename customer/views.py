from django.shortcuts import render

# Create your views here.

def get_customer_master(request):
    return render(request,"customer/customer_master.html")

def get_customer_home(request):
    return render(request,"customer/customer_home.html")
