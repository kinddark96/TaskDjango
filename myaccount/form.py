from django import forms
class RegisterationAdminForm(forms.Form):
    email=forms.EmailField()
    userName=forms.CharField()
    password=forms.CharField()