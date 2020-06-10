from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . forms import EmployerFormInfo, EmployerFormEInfo, CompanyForm, DepartmentForm
from django.views.generic import View, CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .filters import DeptFilter
from .forms import EmployerFormInfo, EmployerFormEInfo, UsersUpdateInfo
from datetime import datetime
from .models import Employer

class DashboardIndex(LoginRequiredMixin, TemplateView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    template_name = 'employer/index.html'

@login_required(login_url='/employer/')
def UserProfileUpdateView(request, pk):
    user = models.User
    model_user = get_object_or_404(user, pk=pk)
    if request.method == 'POST':
        user_form = UsersUpdateInfo(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('employer:user_profile' , kwargs={'pk':model_user.pk}))
        else:
            print(user_form.errors)
    else:
        user_form = UsersUpdateInfo(instance=request.user)
    return render(request, 'employer/user_profile.html', {
        'user_form': user_form,
    })



#----------------------------------------------EMPLOYER VIEWS-------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/employer/')
def EmployerCreateView(request):
    registered = False
    if request.method == 'POST':
        user_form = EmployerFormInfo(data=request.POST)
        employer_form = EmployerFormEInfo(data=request.POST)
        if user_form.is_valid() and employer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = employer_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect('employer:emp_list')
        else:
            print(user_form.errors,employer_form.errors)
    else:
        user_form = EmployerFormInfo()
        employer_form = EmployerFormEInfo()

    return render(request,'employer/employer_Create.html',
                          {'user_form':user_form,
                           'employer_form':employer_form,
                           'registered':registered})

@login_required(login_url='/employer/')
def EmployerUpdateView(request, pk):
    emp_model = models.Employer
    emp = get_object_or_404(emp_model, pk=pk)

    if request.method == 'POST':
        user_form = UsersUpdateInfo(request.POST, instance=emp.user)
        emp_form = EmployerFormEInfo(request.POST, instance=emp)
        if user_form.is_valid() and emp_form.is_valid():
            user_form.save()
            emp_form.save()
            return redirect(reverse('employer:emp_detail' , kwargs={'pk':emp.pk}))
        else:
            print(user_form.errors,emp_form.errors)
    else:
        user_form = UsersUpdateInfo(instance=emp.user)
        emp_form = EmployerFormEInfo(instance=emp)
    return render(request, 'employer/employer_form.html', {
        'user_form': user_form,
        'emp_form': emp_form
    })

class EmployerListView(LoginRequiredMixin,ListView):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'employerList'
    model = models.Employer
    paginate_by = 10
    queryset = models.Employer.objects.all().order_by('-pk')


class EmployerDetailView(DetailView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'employerDetail'
    model = models.Employer
    template_name = 'employer/employer_detail.html'

class EmployerDeleteView(DeleteView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Employer
    success_url = reverse_lazy('employer:emp_list')
#----------------------------------------------COMPANY VIEWS-------------------------------------------------------------------------------------------------------------------------------------------------
class CompanyCreateView(CreateView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('company','createdBy','comments')
    model = models.Company

class CompanyUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('company',)
    model = models.Company

class CompanyListView(ListView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'companyList'
    model = models.Company
    paginate_by = 10
    queryset = models.Company.objects.all().order_by('-pk')


class CompanyDetailView(DetailView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'companyDetail'
    model = models.Company
    template_name = 'employer/company_Detail.html'

class CompanyDeleteView(DeleteView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Company
    success_url = reverse_lazy('employer:com_list')
#----------------------------------------------DEPARTMENT VIEWS-------------------------------------------------------------------------------------------------------------------------------------------------
class DepartmentCreateView(CreateView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('department','createdBy','comments')
    model = models.Department

class DepartmentUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    fields = ('department',)
    model = models.Department

class DepartmentListView(ListView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'departmentList'
    model = models.Department
    paginate_by = 2
    queryset = models.Department.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DeptFilter(self.request.GET, queryset=self.get_queryset())
        return context

class DepartmentDetailView(DetailView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'departmentDetail'
    model = models.Department
    template_name = 'employer/department_detail.html'

class DepartmentDeleteView(DeleteView, LoginRequiredMixin):
    login_url = '/employer/'
    redirect_field_name = 'redirect_to'
    model = models.Department
    success_url = reverse_lazy('employer:dept_list')
# ending of department crud

def employer_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.

                if user.is_staff:
                    login(request,user)
                    # Send the user back to some page.
                    # In this case their homepage.
                    user.last_login = datetime.now()
                    user.save(update_fields=['last_login'])
                    return HttpResponseRedirect(reverse('employer:index'))
                else:
                    messages.error(request, 'You are not authorized to login!')
                    return HttpResponseRedirect(reverse('employer:login'))
            else:
                # If account is not active:
                messages.error(request, 'Your account is not active!')
                # return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, 'Invalid login details supplied!')
            return render(request, 'employer/employer_login.html', {})
            # return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'employer/employer_login.html', {})

@login_required(login_url='/employer/')
def employer_Logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('employer:login'))

@login_required(login_url='/employer/')
def employer_Register(request):
    registered = False
    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        emp_info = EmployerFormInfo(data=request.POST)
        emp_einfo = EmployerFormEInfo(data=request.POST)
        # Check to see both forms are valid
        if emp_info.is_valid() and emp_einfo.is_valid():
            # Save User Form to Database
            user = emp_info.save()
            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()
            # Now we deal with the extra info!
            profile = emp_einfo.save(commit=False)
            # Set One to One relationship between
            profile.user = user
            # Now save model
            profile.save()
            # Registration Successful!
            registered = True
        else:
            # One of the forms was invalid if this else gets called.
            print(emp_info.errors,emp_einfo.errors)
    else:
        # Was not an HTTP post so we just render the forms as blank.
        emp_info = EmployerFormInfo()
        emp_einfo = EmployerFormEInfo()
    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'employer/employer_Register.html',
                          {'emp_info':emp_info,
                           'emp_einfo':emp_einfo,
                           'registered':registered })
