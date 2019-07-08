from django.shortcuts import render

def index(request):
    return render(request,'Inventory/index.html')

def CustomerOrder(request):
    return render(request,'Inventory/CustomerOrder.html')

def Inventory(request):
    return render(request,'Inventory/Inventory.html')

