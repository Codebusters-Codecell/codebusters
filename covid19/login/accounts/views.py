from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import models
def indexView(request):
    return render(request,'index.html')
@login_required
def dashboardView(request):
    if request.method == "POST":
        hid = request.POST.get('hid',False)
        name = request.POST.get('name',False)
        email = request.POST.get('email',False)
        contact = request.POST.get('contact',False)
        country= request.POST.get('country',False)
        state= request.POST.get('state',False)
        city= request.POST.get('city',False)
        count= request.POST.get('count',False)
        address= request.POST.get('address',False)

        print(hid,name,email,contact,country,state,city,count,address)
        ins = models.Data(hid=hid,name=name,email=email,contact=contact,country=country,state=state,city=city,count=count,address=address)
        ins.save()
        print("Data has been saved")
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

def hospitalform(request):
    return render(request,'hospitalform.html')