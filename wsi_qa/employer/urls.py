from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = 'employer'

urlpatterns = [
#----------------------------------------------LOGIN/LOGOUT URLS-------------------------------------------------------------------------------------------------------------------------------------------------
    path('', views.employer_login, name='login'),
    path('employer_Logout/', views.employer_Logout, name='employer_Logout'),
#----------------------------------------------dashboard URLS-------------------------------------------------------------------------------------------------------------------------------------------------
    path('dashboard/',views.DashboardIndex.as_view(), name='index'),
    path('user_profile/<int:pk>/', views.UserProfileUpdateView, name='user_profile'),
#----------------------------------------------forgot password in login page-------------------------------------------------------------------------------------------------------------------------------------------------
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='employer/password_reset.html'),name='reset_password'),
#----------------------------------------------change password inside dashboard-------------------------------------------------------------------------------------------------------------------------------------------------
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='employer/change_password.html', success_url='/employer/'), name='change_password'),
#----------------------------------------------EMPLOYER URLS-------------------------------------------------------------------------------------------------------------------------------------------------
    path('employer_Create/', views.EmployerCreateView, name='emp_create'),
    path('employer_List/', views.EmployerListView.as_view(),name='emp_list'),
    path('employer_Delete/<int:pk>/',views.EmployerDeleteView.as_view(),name='emp_delete'),
    path('employer_Detail/<int:pk>/',views.EmployerDetailView.as_view(),name='emp_detail'),
    path('employer_Update/<int:pk>/', views.EmployerUpdateView, name='emp_update'),
#----------------------------------------------COMPANY URLS-------------------------------------------------------------------------------------------------------------------------------------------------
    path('company_Create/', views.CompanyCreateView.as_view(),name='com_create'),
    path('company_Update/<int:pk>/',views.CompanyUpdateView.as_view(),name='com_update'),
    path('company_List/', views.CompanyListView.as_view(),name='com_list'),
    path('company_Detail/<int:pk>/',views.CompanyDetailView.as_view(),name='com_detail'),
    path('company_Delete/<int:pk>', views.CompanyDeleteView.as_view(), name='com_delete'),
#----------------------------------------------DEPARTMENT URLS-------------------------------------------------------------------------------------------------------------------------------------------------
    path('department_Create/', views.DepartmentCreateView.as_view(),name='dept_create'),
    path('department_Update/<int:pk>/',views.DepartmentUpdateView.as_view(), name='dept_update'),
    path('department_List/', views.DepartmentListView.as_view(),name='dept_list'),
    path('department_Detail/<int:pk>/',views.DepartmentDetailView.as_view(), name='dept_detail'),
    path('department_Delete/<int:pk>', views.DepartmentDeleteView.as_view(), name='dept_delete'),
]
