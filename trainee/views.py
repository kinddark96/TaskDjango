from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def traineeList(req):
    return HttpResponse('Hello List Trainee')

def traineeAdd(req):
    return render(req,'index.html')

def traineeUpdate(req,id):
    return HttpResponse('Hello Update Trainee')
def traineeDelete(req,ID):
    return HttpResponse('Hello Delete Trainee')