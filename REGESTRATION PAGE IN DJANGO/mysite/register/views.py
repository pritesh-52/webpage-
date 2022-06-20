from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    return render(request,'register.html')    #Register page

def userregister(request):
    if request.method=="POST":
        fname =request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        us=user.objects.filter(Email=email)

        if us:
            message="user already exists"
            return render(request,'register.html',{'msg':message})
        else:
            if password==cpassword:
                newuser=user.objects.create(Fname=fname,Lname=lname,Email=email,Contact=contact,Password=password)
                message="user registred sucessfully"
                return  render(request,'login.html',{'msg':message})
            else:
                message="password and conform password does not match"
                return render(request, 'register.html', {'msg': message})


def loginpage(request):
    return  render(request,'login.html')

def userlogin(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]

        us=user.objects.get(Email=email)
        if us:
            if us.Password==password:
                request.session['firstname']=us.Fname
                request.session['lastname']=us.Lname
                return render(request,'home.html')
            else:
                message="password  does not match"
                return render(request,'login.html',{'ms':message})
        else:
            message="user does not match"
            return render(request,'register.html',{'ms':message})










