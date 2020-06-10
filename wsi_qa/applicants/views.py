from django.shortcuts import render
from . import models
from django.views.generic import View, CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . forms import ApplicantsFormInfo, ApplicantsFormEInfo, UsersApplicantsFormUpdate
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardIndex(LoginRequiredMixin, TemplateView):
    login_url = '/applicants/'
    redirect_field_name = 'redirect_to'
    template_name = 'applicants/index.html'

def ApplicantLogin(request):
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
                login(request,user)
                    # Send the user back to some page.
                    # In this case their homepage.
                user.last_login = datetime.now()
                user.save(update_fields=['last_login'])
                return HttpResponseRedirect(reverse('applicants:index'))
            else:
                # If account is not active:
                messages.error(request, 'Your account is not active!')
                # return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, 'Invalid login details supplied!')
            return render(request, 'applicants/applicants_Login.html', {})
            # return HttpResponse("Invalid login details supplied.")
    else:
        #Nothing has been provided for username or password.
        return render(request, 'applicants/applicants_Login.html', {})

@login_required(login_url='/applicant/')
def ApplicantLogout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('applicants:applicants_Login'))


# Create your views here.
def ApplicantsCreateView(request):
    registered = False
    if request.method == 'POST':
        user_form = ApplicantsFormInfo(data=request.POST)
        applicants_form = ApplicantsFormEInfo(data=request.POST)
        if user_form.is_valid() and applicants_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = applicants_form.save(commit=False)
            profile.user = user
            profile.save()
            # registered = True
            return redirect('applicants:applicants_list')
        else:
            print(user_form.errors,applicants_form.errors)
    else:
        user_form = ApplicantsFormInfo()
        applicants_form = ApplicantsFormEInfo()

    return render(request,'applicants/applicants_Create.html',
                          {'user_form':user_form,
                           'applicants_form':applicants_form,
                           'registered':registered})

class ApplicantsListView(ListView):
    context_object_name = 'applicantsList'
    model = models.Applicants
    paginate_by = 10
    queryset = models.Applicants.objects.all().order_by('-pk')

class ApplicantDetailView(DetailView):
    context_object_name = 'applicantDetail'
    model = models.Applicants
    template_name = 'applicants/applicants_Detail.html'

class ApplicantDeleteView(DeleteView):
    model = models.Applicants
    success_url = reverse_lazy('applicants:applicants_list')

def ApplicantsUpdateView(request, pk):
    model_applicant = models.Applicants
    applicant = get_object_or_404(model_applicant, pk=pk)
    if request.method == 'POST':
        user_form = UsersApplicantsFormUpdate(request.POST, instance=applicant.user)
        applicants_form = ApplicantsFormEInfo(request.POST, instance=applicant)
        if user_form.is_valid() and applicants_form.is_valid():
            user_form.save()
            applicants_form.save()
            return redirect(reverse('applicants:applicants_detail' , kwargs={'pk':applicant.pk}))
        else:
            print(user_form.errors,applicants_form.errors)
    else:
        user_form = UsersApplicantsFormUpdate(instance=applicant.user)
        applicants_form = ApplicantsFormEInfo(instance=applicant)
    return render(request, 'applicants/applicants_form.html', {
        'user_form': user_form,
        'applicants_form': applicants_form
    })
