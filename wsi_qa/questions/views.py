from django.shortcuts import render
from django.views.generic import View, CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from . import models
from . models import QuestionForm
from . resources import QuestionsResource
import csv, io
from django.contrib import messages
# Create your views here.
#-------------------------------------------- For the question--------------------------------------------------------
class QuestionListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'questionList'
    model = models.Questions
    paginate_by = 10
    queryset = models.Questions.objects.all().order_by('-pk')


class QuestionDetailView(LoginRequiredMixin,DetailView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'questionDetail'
    model = models.Questions
    template_name = 'questions/questions_Detail.html'

class QuestionCreateView(LoginRequiredMixin,CreateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    # fields = ('question', 'process', 'category', 'area', 'skill', 'difficulty', 'choice', 'answer', 'comments')
    form_class = QuestionForm
    model = models.Questions

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    form_class = QuestionForm
    model = models.Questions

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class QuestionDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Questions
    success_url = reverse_lazy('questions:question_List')
#-------------------------------------------- For the choices--------------------------------------------------------
class ChoiceListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'choiceList'
    model = models.Choice
    paginate_by = 10
    queryset = models.Choice.objects.all().order_by('-pk')

class ChoiceDetailView(LoginRequiredMixin,DetailView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'choiceDetail'
    model = models.Choice
    template_name = 'questions/choice_Detail.html'

class ChoiceCreateView(LoginRequiredMixin,CreateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('choices', 'comments',)
    model = models.Choice

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)


class ChoiceUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('choices',)
    model = models.Choice
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class ChoiceDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Choice
    success_url = reverse_lazy('questions:choice_List')
#-------------------------------------------- For the process--------------------------------------------------------
class ProcessListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'processList'
    model = models.Process
    paginate_by = 10
    queryset = models.Process.objects.all().order_by('-pk')


class ProcessDetailView(LoginRequiredMixin,DetailView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'processDetail'
    model = models.Process
    template_name = 'questions/process_Detail.html'

class ProcessCreateView(LoginRequiredMixin,CreateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('process', 'comments')
    model = models.Process

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class ProcessUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('process',)
    model = models.Process
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class ProcessDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Process
    success_url = reverse_lazy('questions:process_List')
#-------------------------------------------- For the Category--------------------------------------------------------
class CategoryListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'categoryList'
    model = models.Category
    paginate_by = 10
    queryset = models.Category.objects.all().order_by('-pk')


class CategoryDetailView(LoginRequiredMixin,DetailView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'caregoryDetail'
    model = models.Category
    template_name = 'questions/category_Detail.html'

class CategoryCreateView(LoginRequiredMixin,CreateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('category', 'comments')
    model = models.Category
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('category',)
    model = models.Category
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class CategoryDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Category
    success_url = reverse_lazy('questions:category_List')
#-------------------------------------------- For the Area--------------------------------------------------------
class AreaListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'areaList'
    model = models.Area
    paginate_by = 10
    queryset = models.Area.objects.all().order_by('-pk')


class AreaDetailView(LoginRequiredMixin,DetailView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'areaDetail'
    model = models.Area
    template_name = 'questions/area_Detail.html'

class AreaCreateView(LoginRequiredMixin,CreateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('area', 'comments')
    model = models.Area
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class AreaUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('area',)
    model = models.Area
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class AreaDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Area
    success_url = reverse_lazy('questions:area_List')
#-------------------------------------------- For the Skill--------------------------------------------------------
class SkillListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'skillList'
    model = models.Skill
    paginate_by = 10
    queryset = models.Skill.objects.all().order_by('-pk')


class SkillDetailView(LoginRequiredMixin,DetailView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'skillDetail'
    model = models.Skill
    template_name = 'questions/skill_Detail.html'

class SkillCreateView(LoginRequiredMixin,CreateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('skill', 'comments')
    model = models.Skill

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class SkillUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('skill',)
    model = models.Skill
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class SkillDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Skill
    success_url = reverse_lazy('questions:skill_List')
#-------------------------------------------- For the Difficulty--------------------------------------------------------
class DifficultyListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'difficultyList'
    model = models.Difficulty
    paginate_by = 10
    queryset = models.Difficulty.objects.all().order_by('-pk')


class DifficultyDetailView(LoginRequiredMixin,DetailView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'difficultyDetail'
    model = models.Difficulty
    template_name = 'questions/difficulty_Detail.html'

class DifficultyCreateView(LoginRequiredMixin,CreateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('difficulty', 'comments')
    model = models.Difficulty
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class DifficultyUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('difficulty',)
    model = models.Difficulty
    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class DifficultyDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Difficulty
    success_url = reverse_lazy('questions:difficulty_List')

def import_data(request):
    template = 'questions/import.html'

    prompt = {
        'order': 'Order of the CSV file should be question, process, category, area, skill, difficulty, choice, answer, createdBy, createdDate, comments'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = models.Questions.objects.update_or_create(
            question = column[0]
        )
    context = {}
    return render(request, template, context)
