from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
def loginAcc(req):
    context={}
    if(req.method=='POST'):
        checkUser=Users.objects.filter(email=req.POST['email'],password=req.POST['password'])
        if(len(checkUser)!=0):
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
        
    return render(req,'register.html')