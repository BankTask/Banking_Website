from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.generic import CreateView

from django.forms import  ModelForm

def index(request):
    return render(request,'index.html')
def login(request):
    if request.method=='POST':
        username=request.POST['login']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"home.html")

        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('/login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')


    return render(request,"register.html")

def home(request):
    return render(request,"home.html")

def form(request):
    if request.method == "POST":
        print( "Application Accepted")
    return render(request,"form.html")

def logout(request):
    auth.logout(request)
    return redirect('/')