from django import forms
from django.contrib.auth.models import User
from .models import Applicants
from datetime import datetime

class ApplicantsFormInfo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',"password")


class ApplicantsFormEInfo(forms.ModelForm):
    createdDate = forms.DateField(initial=datetime.now, disabled = True, label='Created Date')
    class Meta():
        model = Applicants
        fields = ('createdBy','createdDate','comments')
        labels = {
            'createdBy' : 'Created By',
        }

class UsersApplicantsFormUpdate(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
