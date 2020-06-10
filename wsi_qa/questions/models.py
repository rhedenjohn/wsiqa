from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

User = get_user_model()
# Create your models here.

class Choice(models.Model):
    choices = models.CharField(max_length=500 , null=True, blank=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', verbose_name=('Created By'))
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.choices

    def get_absolute_url(self):
        return reverse("questions:choice_Detail",kwargs={'pk':self.pk})

class Questions(models.Model):
    question = models.CharField(max_length=500)
    process = models.ForeignKey('Process', on_delete=models.CASCADE, related_name='+',  blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='+',  blank=True, null=True)
    area = models.ForeignKey('Area', on_delete=models.CASCADE, related_name='+',  blank=True, null=True)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, related_name='+',  blank=True, null=True)
    difficulty = models.ForeignKey('Difficulty', on_delete=models.CASCADE, related_name='+',  blank=True, null=True)
    choice = models.ManyToManyField(Choice, related_name='choice',  blank=True, null=True)
    answer = models.ManyToManyField(Choice, related_name='answer',  blank=True, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', verbose_name=('Created By'), blank=True, null=True)
    createdDate = models.DateField(default=datetime.now, blank=True, null=True)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("questions:question_Detail",kwargs={'pk':self.pk})

class Process(models.Model):
    process = models.CharField(max_length=500, default='None')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+' , verbose_name=('Created By'))
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.process

    def get_absolute_url(self):
        return reverse("questions:process_Detail", kwargs={'pk':self.pk})

class Category(models.Model):
    category = models.CharField(max_length=500, default='None')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+' , verbose_name=('Created By'))
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("questions:category_Detail", kwargs={'pk':self.pk})

class Area(models.Model):
    area = models.CharField(max_length=500, default='None')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+' , verbose_name=('Created By'))
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.area

    def get_absolute_url(self):
        return reverse("questions:area_Detail", kwargs={'pk':self.pk})

class Skill(models.Model):
    skill = models.CharField(max_length=500, default='None')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+' , verbose_name=('Created By'))
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.skill

    def get_absolute_url(self):
        return reverse("questions:skill_Detail", kwargs={'pk':self.pk})

class Difficulty(models.Model):
    difficulty = models.CharField(max_length=500, default='None')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+' , verbose_name=('Created By'))
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        return self.difficulty

    def get_absolute_url(self):
        return reverse("questions:difficulty_Detail", kwargs={'pk':self.pk})

class QuestionForm(ModelForm):

    class Meta:
        model = Questions
        fields = ('question', 'process', 'category', 'area', 'skill', 'difficulty', 'choice', 'answer', 'comments')

    def __init__(self, *args, **kwargs):

        super(QuestionForm, self).__init__(*args, **kwargs)

        self.fields["choice"].widget = CheckboxSelectMultiple()
        self.fields["choice"].queryset = Choice.objects.all()

        self.fields["answer"].widget = CheckboxSelectMultiple()
        self.fields["answer"].queryset = Choice.objects.all()
