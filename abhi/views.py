from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import data
from django.contrib import messages
from django.contrib.auth.models import User, auth




def start(request):
    info=request.POST["blank1"]
    account_id=request.user.id
    if info=="":
        return redirect("Home")
    else:
        o_ref=data(information=info,account_id=account_id)
        o_ref.save()
        infodata=data.objects.all()
        return redirect("Home")



def delete(request,id):
    obj=data.objects.get(id=id)
    obj.delete()
    return redirect("Home")


def home(request):
    

    infodata=data.objects.all()
    account_i=request.user.id
    name=request.user.first_name
    
    return render(request,"home.html",{'infodata': infodata,'acc':account_i,'name':name})



def dynamic(request,pk_test):
    obj=data.objects.get(pk=pk_test)
    obj2=data.objects.all()
    acc=request.user.id
    name=request.user.first_name
    return render(request,"EditItem.html",{'obje':obj,'obj2':obj2,'pk_test':pk_test,'acc':acc,'name':name})



def editSave(request,pk):
    info=request.POST["edititem"]
    obj=data.objects.get(pk=pk)
    obj.information=info

    obj.save()
    return redirect("Home")

def mark(request,my_pk):
    obj=data.objects.get(pk=my_pk)
    if obj.itemMark==True:
        obj.itemMark=False
        obj.save()
    else:
        obj.itemMark=True
        obj.save()
    return redirect("Home")
