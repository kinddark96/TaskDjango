from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def traineeList(req):
     trainees=[(1,"trainee1"),(2,"trainee2"),(3,"trainee3")]
     context={}
     context['trainees']=trainees
     return render(req,'listTrainee.html',context)

def traineeAdd(req):
    return render(req,'addTrainee.html')

def traineeUpdate(req,id):
    return render(req,'updateTrainee.html')
def traineeDelete(req,ID):
    return render(req,'deleteTrainee.html')