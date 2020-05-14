from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from abhi.models import data

def register(request):
    if request.method =='POST':
        
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['Username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Exists,Try another.')
                return redirect("/")
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=firstname,last_name=lastname)
                user.save()
                messages.info(request,'User created')
                return redirect("login")
        else:
            messages.info(request,'Password does not match,try again.')
            return redirect("/")
            
    else:
        return render(request,"registration.html")

def login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print(request.user.id)
            
            return redirect("Home")
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    messages.info(request,"You are logged out now")
    return redirect("/")


