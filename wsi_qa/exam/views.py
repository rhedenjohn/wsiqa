from django.shortcuts import render
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import ApplicantsExamForm
from bootstrap_datepicker_plus import DateTimePickerInput
from django.db.models import Q
#-------------------------------------------------------Exam Views----------------------------------------------------------------------------------------------------
class ExamCreateView(LoginRequiredMixin,CreateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('exam', 'questions', 'timeDuration', 'comments')
    model = models.Exams

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class ExamListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'examList'
    model = models.Exams
    paginate_by = 10;
    # queryset = models.Exams.objects.all().order_by('-pk')

    def get_queryset(self):

        if 'search' in self.request.GET:
            objects = models.Exams.objects.filter(
                Q(exam__icontains=self.request.GET['search']) |
                Q(timeDuration__icontains=self.request.GET['search'])
                )
        else:
            objects = models.Exams.objects.all()

        return objects

class ExamDetailView(LoginRequiredMixin,DetailView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'examDetail'
    model = models.Exams
    template_name = 'exam/exams_detail.html'

class ExamDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Exams
    success_url = reverse_lazy('exam:list_exam')
    select_related = ('ApplicantExam_exam',)

class ExamUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('exam', 'timeDuration',)
    model = models.Exams
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)
#-------------------------------------------------------Applicant Exam Views----------------------------------------------------------------------------------------------------
class ApplicantExamCreateView(LoginRequiredMixin,CreateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    form_class = ApplicantsExamForm
    model = models.ApplicantExam


class ApplicantExamListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'applicantExamList'
    model = models.ApplicantExam
    paginate_by = 10;
    queryset = models.ApplicantExam.objects.all().order_by('-pk')


class ApplicantExamDetailView(LoginRequiredMixin,DetailView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'applicantExamDetail'
    model = models.ApplicantExam
    template_name = 'exam/applicantExam_detail.html'

class ApplicantExamDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'applicantDelete'
    model = models.ApplicantExam
    success_url = reverse_lazy('exam:applicantExam_List')

class ApplicantExamUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    form_class = ApplicantsExamForm
    model = models.ApplicantExam
