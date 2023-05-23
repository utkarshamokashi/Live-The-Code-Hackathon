from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from .models import Config, Info, Customized_Info
import json
import os
from sawo import createTemplate, getContext, verifyToken


load = ''
loaded = 0

def setPayload(payload):
    global load
    load = payload

def setLoaded(reset=False):
    global loaded
    if reset:
        loaded=0
    else:
        loaded+=1

    
createTemplate('templates/partials')



# def index(request):
#     config = Config.objects.order_by('_api_key')[:1]
#     setLoaded()
#     setPayLoad(load if loaded<2 else '')
#     context = {"sawo":getContext(config,'main/recive') if (config) else (), "load":load, "Title":"Home"}
#     return render(request,"signin.html",context)

def index(request):
    return render(request,"index.html")

def signin(request):
    setLoaded()
    setPayload(load if loaded<2 else '')
    print(os.environ.get('api_key'))
    config = {
                "auth_key": os.environ.get('api_key'),
                "identifier": "email",
                "to": "receive"
    }
    context = {"sawo":config,"load":load,"title":"Home"}
    return render(request,'signin.html',context)

def info(request):
    if request.method=='POST':
        form=Info(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        ins=Info(name=name,email=email)
        ins.save()
        messages.success(request, 'Profile is set up Welcome to the Dashboard')
        return redirect('dashboard')
    else:
        form = Info()
    return render(request,'info.html')

def dashboard(request):
    db_list = Customized_Info.objects.all()
    return render(request,"dashboard.html",{"db_list":db_list})

def form(request):
    if request.method=='POST':
        form =Customized_Info(request.POST)
        c_name=request.POST.get('c_name')
        logo=request.POST.get('logo')
        bg_img=request.POST.get('bg_img')
        url=request.POST.get('url')
        c_url=request.POST.get('c_url')
        desc=request.POST.get('desc')
        ins=Customized_Info(c_name=c_name,logo=logo,bg_img=bg_img,url=url,c_url=c_url,desc=desc)
        ins.save()
        messages.success(request, 'Profile is set up Welcome to the Community')
        
        return redirect('community')
    else:
        form = Customized_Info()
    return render(request,'form.html')

def community(request):
    customized_data = Customized_Info.objects.all()
    return render(request,"template.html",{"customized_data":customized_data})

def update_id(request):
     data = Customized_Info.objects.all()
     return render(request, "template.html",{"data":data})

def aboutUs(request):
    return render(request,'aboutUs.html')
