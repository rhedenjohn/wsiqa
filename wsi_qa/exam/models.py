from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from applicants.models import Applicants
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import ModelForm
from questions.models import Questions
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
# from django.contrib.admin import widgets
# from django import forms


User = get_user_model()

class Exams(models.Model):
    exam = models.CharField(max_length=500, default='None')
    timeDuration = models.IntegerField(null=True, blank=True)
    questions = models.ManyToManyField(Questions, related_name='questions',  blank=True, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+' , verbose_name=('Created By'))
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.exam

    def get_absolute_url(self):
        return reverse("exam:detail_exam",kwargs={'pk':self.pk})

    class Meta():
        ordering = ["-pk"]

class ApplicantExam(models.Model):
    applicant = models.ForeignKey(Applicants, related_name='ApplicantExam_applicant', on_delete=models.CASCADE)
    exam = models.ManyToManyField(Exams, related_name='applicant_Exam')
    exam_Date = models.DateField(default=datetime.now)
    expire_Date = models.DateField(default=datetime.now)
    score = models.IntegerField()

    def __str__(self):
        return str(self.applicant)

    def save(self, *args, **kwargs):
        if not self.id:
            self.name = self.user.first_name + self.user.last_name
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('exam:applicantExam_Detail', kwargs={'pk':self.pk})

class ApplicantsExamForm(ModelForm):

    class Meta:
        model = ApplicantExam
        fields = ('applicant', 'exam', 'exam_Date', 'expire_Date', 'score',)
        widgets = {
            'exam_Date': DatePickerInput(),
            'expire_Date': DatePickerInput(),
        }

    def __init__(self, *args, **kwargs):

        super(ApplicantsExamForm, self).__init__(*args, **kwargs)

        self.fields["exam"].widget = CheckboxSelectMultiple()
        self.fields["exam"].queryset = Exams.objects.all()
