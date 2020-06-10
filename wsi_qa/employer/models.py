from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    createdBy = models.ForeignKey(to='Employer', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse("employer:emp_detail",kwargs={'pk':self.pk})

class Department(models.Model):
    department = models.CharField(max_length=200)
    createdBy= models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='+', verbose_name=('Created By'))
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.department

    def get_absolute_url(self):
        return reverse('employer:dept_detail', kwargs={'pk':self.pk})

class Company(models.Model):
    company = models.CharField(max_length=200)
    createdBy = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='+', verbose_name=('Created By'))
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('employer:com_detail', kwargs={'pk':self.pk})
