from django.urls import path
from . import views
app_name = 'applicants'

urlpatterns = [
    path('index/', views.DashboardIndex.as_view(), name='index'),
    path('', views.ApplicantLogin, name='applicants_Login'),
    path('logout/', views.ApplicantLogout, name='applicants_Logout'),
    path('applicants_Create/', views.ApplicantsCreateView, name='applicants_create'),
    path('applicants_List/', views.ApplicantsListView.as_view(), name='applicants_list'),
    path('applicants_Detail/<int:pk>/', views.ApplicantDetailView.as_view(), name='applicants_detail'),
    path('applicants_Delete/<int:pk>/', views.ApplicantDeleteView.as_view(), name='applicants_delete'),
    path('applicants_Update/<int:pk>/', views.ApplicantsUpdateView, name='applicants_update'),
]
