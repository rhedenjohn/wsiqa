from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
#-------------------------------------------------------Exam URLS----------------------------------------------------------------------------------------------------
    path('create_Exam/', views.ExamCreateView.as_view(), name='create_exam'),
    path('list_Exam/', views.ExamListView.as_view(), name='list_exam'),
    path('detail_Exam/<int:pk>', views.ExamDetailView.as_view(), name='detail_exam'),
    path('delete_Exam/<int:pk>', views.ExamDeleteView.as_view(), name='delete_exam'),
    path('update_Exam/<int:pk>', views.ExamUpdateView.as_view(), name='update_exam'),
#-------------------------------------------------------Applicant Exam URLS----------------------------------------------------------------------------------------------------
    path('applicantExam_Create/', views.ApplicantExamCreateView.as_view(), name='applicantExam_Create'),
    path('applicantExam_List/', views.ApplicantExamListView.as_view(), name='applicantExam_List'),
    path('applicantExam_Detail/<int:pk>/', views.ApplicantExamDetailView.as_view(), name='applicantExam_Detail'),
    path('applicantExam_Delete/<int:pk>/', views.ApplicantExamDeleteView.as_view(), name='applicantExam_Delete'),
    path('applicantExam_Update/<int:pk>/', views.ApplicantExamUpdateView.as_view(), name='applicantExam_Update'),
]
