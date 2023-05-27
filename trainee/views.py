from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def traineeList(req):
     trainees=[(1,"trainee1"),(2,"trainee2"),(3,"trainee3")]
     context={}
     context['trainees']=trainees
     return render(req,'listTrainee.html',context)

def traineeAdd(req):
    return render(req,'addTrainee.html')

def traineeUpdate(req,id):
    context={}
    context[id]=id
    # return render(req,'updateTrainee.html',context)
    return HttpResponseRedirect('/Trainee')
def traineeDelete(req,ID):
    context={}
    context[id]=ID
    return HttpResponseRedirect('/Trainee')
    # return render(req,'deleteTrainee.html',context)