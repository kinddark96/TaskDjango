from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from course.models import *
# Create your views here.
def traineeList(req):
     if('username' in req.session):
        trainees=Trainees.objects.all()
        context={}
        context['trainees']=trainees
        return render(req,'listTrainee.html',context)
     else:
         return HttpResponseRedirect('/')
def traineeAdd(req):
    if('username' in req.session):
        context={}
        context['courses']=Courses.objects.all()
        if(req.method=='POST'):
            
            course=Courses.objects.get(id=req.POST['courses'])
            Trainees.objects.create(traineeName=req.POST['trainee'],courseID=course)
            return HttpResponseRedirect('/Trainee')
        return render(req,'addTrainee.html',context)
    else:
         return HttpResponseRedirect('/')

def traineeUpdate(req,id):
    if('username' in req.session):
        context={}
        context['courses']=Courses.objects.all()
        context['Trainee']=Trainees.objects.get(id=id)
        if(req.method=='POST'):
            course=Courses.objects.get(id=req.POST['courses'])
            Trainees.objects.filter(id=id).update(traineeName=req.POST['trainee'],courseID=course)
        return render(req,'updateTrainee.html',context)
    else:
         return HttpResponseRedirect('/')
def traineeDelete(req,ID):
    if('username' in req.session):
        Trainees.objects.filter(id=ID).delete()
        return HttpResponseRedirect('/Trainee')
    else:
         return HttpResponseRedirect('/')
