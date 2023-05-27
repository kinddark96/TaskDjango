from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def loginAcc(req):
    return render(req,'login.html')
def logOutAcc(req):
    return HttpResponse("Hello Again")
def registerAcc(req):
    return render(req,'register.html')