from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courseList(req):
    if('username' in req.session):
          courses=[(1,"course1"),(2,"course2"),(3,"course3")]
          context={}
          context['courses']=courses
          return render(req,'listCourse.html',context)

def courseAdd(req):
     if('username' in req.session):
          return render(req,'addCourse.html')

def courseUpdate(req,id):
     if('username' in req.session):
          return render(req,'updateCourse.html')

def courseDelete(req,ID):
    if('username' in req.session):
          return render(req,'deleteCourse.html')