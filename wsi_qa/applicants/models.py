from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from exam.models import Exams
from questions.models import Questions, Choice
User = get_user_model()

class Applicants(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    createdDate = models.DateField(default=datetime.now)
    comments = models.CharField(max_length=500, default='None')

    def __str__(self):
        fn = self.user.first_name + ' ' + self.user.last_name
        return fn

    def get_absolute_url(self):
        return reverse("applicants:applicants_detail",kwargs={'pk':self.pk})

class Answers(models.Model):
    user = models.ForeignKey(Applicants, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)