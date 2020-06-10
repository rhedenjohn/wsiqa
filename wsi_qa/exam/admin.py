from django.contrib import admin
from . models import Exams, ApplicantExam
from . forms import ExamForm
# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    form = ExamForm

admin.site.register(Exams, ExamAdmin)
admin.site.register(ApplicantExam)
