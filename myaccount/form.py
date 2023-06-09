from django import forms
class RegisterationAdminForm(forms.Form):
    
    email=forms.EmailField(label="Email",widget=forms.EmailInput,max_length=35)
    username=forms.CharField()
    password=forms.CharField(label="Password",widget=forms.PasswordInput(),max_length=15)