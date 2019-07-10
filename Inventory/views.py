
from django.shortcuts import render
from .models import Status, Email

def index(request):
    return render(request,'Inventory/index.html')

def customer(request):
    return render(request,'Inventory/CustomerOrder.html')

def insert(request):
    Create_val = request.POST.get("Create_val", False)
    Customer_Name=request.POST.get("Customer_Name",False)
    Reference_Order=request.POST.get("Reference_Order",False)
    Products=request.POST.get("Products",False)
    status = Status(created=Create_val,customer_name=Customer_Name,reference_order=Reference_Order, products=Products)
    status.save()
    return render(request,'Inventory/CustomerOrder.html')

def storage(request):
    all_status= Status.objects.all()
    return render(request,'Inventory/Inventory.html',{'storage':all_status})

def submit(request):
    emailid=request.POST.get("email")

    email = Email(email_id=emailid)
    email.save()
    return render(request,'Inventory/index.html')