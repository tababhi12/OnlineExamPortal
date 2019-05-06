from django import forms
from candidate.models import Candidate
from django.contrib.auth.models import User
class UserForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = Candidate
         fields = ('First_name','Last_name','Sex','Phone','Experience','Notice_period','Skill','Source',)