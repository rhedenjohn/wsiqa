from django import forms
from django.contrib.auth.models import User
from .models import Employer, Department, Company
from datetime import datetime

class EmployerFormInfo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',"password", 'is_staff')

    def __init__(self, *args, **kwargs):
        super(EmployerFormInfo, self).__init__(*args, **kwargs)
        self.fields['is_staff'].disabled = True
        self.fields['is_staff'].initial = True



class EmployerFormEInfo(forms.ModelForm):
    createdDate = forms.DateField(initial=datetime.now, disabled = True, label='Created Date')
    # first_name = forms.CharField(max_length=255, required=True)
    class Meta():
        model = Employer
        fields = ('department','company','createdBy','createdDate','comments')
        labels = {
            'createdBy' : 'Created By',
            'createdDate' : 'Created Date'
        }

class UsersUpdateInfo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class DepartmentForm(forms.ModelForm):
    # createdDate = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta():
        model = Department
        fields = ('department','createdBy','createdDate','comments')
        labels = {
            'createdBy' : 'Created By',
            'createdDate' : 'Created Date'
        }

class CompanyForm(forms.ModelForm):
    class Meta():
        model = Company
        fields = ('company','createdBy','createdDate','comments')
