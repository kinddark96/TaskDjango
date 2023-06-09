from django import forms
from .models import *
from django.contrib.auth.models import * 
class AddTrainForm(forms.Form):
    traineeName=forms.CharField(label="Trainee Name",max_length=35)
    
    # courseID=forms.IntegerField(label="Course ID")


class updateTraineeModelForm(forms.ModelForm):
    class Meta:
        model=Trainees
        fields='__all__'
        ## id
        ## traineeName
        ## courseID
       