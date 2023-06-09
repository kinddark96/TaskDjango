from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import *
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth import login, authenticate
# Create your views here.
def loginAcc(req):
    context={}
    if(req.method=='POST'):
        checkUser=Users.objects.filter(userName=req.POST['email'],password=req.POST['password'])
        userObject=authenticate(username=req.POST['email'],password=req.POST['password'])
        if(req.POST['identify']=='admin'):
            if(len(checkUser)!=0 and userObject is not  None):
                req.session['username']=checkUser[0].userName
                login(req,userObject)

                return HttpResponseRedirect('/admin')
            
            else:
                inputEmail=req.POST['email']
                context['msg']=f'Theres no Admin call {inputEmail}'
        else:
            if(len(checkUser)!=0 ):
                req.session['username']=checkUser[0].userName
                return HttpResponseRedirect('/Trainee')
            else:
                inputEmail=req.POST['email']
                context['msg']=f'Theres no user call {inputEmail}'
    return render(req,'login.html',context)
def logOut(req):
    req.session.clear()
    return HttpResponseRedirect("/")
def registerAcc(req):
    context={}
    if (req.method == 'POST'):
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        userInfo=Users(userName=username)
        userInfo.password=password
        userInfo.email=email
        userInfo.save()    
    return render(req,'register.html',context)

def registerAdmin(req):
    f=RegisterationAdminForm()
    context={}
    context['form']=f
    if (req.method=='POST'):
        f=RegisterationAdminForm(req.POST)
        if(f.is_bound ):
            User.objects.create_superuser(username=req.POST['username'],password=req.POST['password'],email=req.POST['email'])
            return HttpResponseRedirect('/admin')
    return render(req,'registAdmin.html',context)