from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courseList(req):
    return HttpResponse('Hello List course')

def courseAdd(req):
    return HttpResponse('Hello Add course')

def courseUpdate(req,id):
    return HttpResponse('Hello Update course')
def courseDelete(req,ID):
    return HttpResponse('Hello Delete course')