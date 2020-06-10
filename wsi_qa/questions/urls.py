from django.urls import path
from django.urls import re_path
from . import views

app_name = 'questions'
urlpatterns = [
#----------------------------------------------Question URLS------------------------------------------------------------
    path('', views.QuestionListView.as_view(), name='question_List'),
    path('question_Detail/<int:pk>/',views.QuestionDetailView.as_view(),name='question_Detail'),
    path('question_Create/',views.QuestionCreateView.as_view(), name='question_Create'),
    path('question_Update/<int:pk>/', views.QuestionUpdateView.as_view(), name='question_Update'),
    path('question_Delete/<int:pk>/',views.QuestionDeleteView.as_view(),name='question_Delete'),
    path('question_Import/', views.import_data, name='import_file'),
#----------------------------------------------Choice URLS------------------------------------------------------------
    path('choice_List/', views.ChoiceListView.as_view(), name='choice_List'),
    path('choice_Detail/<int:pk>/', views.ChoiceDetailView.as_view(), name='choice_Detail'),
    path('choice_Create/',views.ChoiceCreateView.as_view(), name='choice_Create'),
    path('choice_Update/<int:pk>/',views.ChoiceUpdateView.as_view(), name='choice_Update'),
    path('choice_Delete/<int:pk>/',views.ChoiceDeleteView.as_view(),name='choice_Delete'),
#----------------------------------------------Process URLS------------------------------------------------------------
    path('process_List/', views.ProcessListView.as_view(), name='process_List'),
    path('process_Detail/<int:pk>/', views.ProcessDetailView.as_view(), name='process_Detail'),
    path('process_Create/',views.ProcessCreateView.as_view(), name='process_Create'),
    path('process_Update/<int:pk>/',views.ProcessUpdateView.as_view(), name='process_Update'),
    path('process_Delete/<int:pk>/',views.ProcessDeleteView.as_view(),name='process_Delete'),
#----------------------------------------------Category URLS------------------------------------------------------------
    path('category_List/', views.CategoryListView.as_view(), name='category_List'),
    path('category_Detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category_Detail'),
    path('category_Create/',views.CategoryCreateView.as_view(), name='category_Create'),
    path('category_Update/<int:pk>/',views.CategoryUpdateView.as_view(), name='category_Update'),
    path('category_Delete/<int:pk>/',views.CategoryDeleteView.as_view(),name='category_Delete'),
#----------------------------------------------Area URLS------------------------------------------------------------
    path('area_List/', views.AreaListView.as_view(), name='area_List'),
    path('area_Detail/<int:pk>/', views.AreaDetailView.as_view(), name='area_Detail'),
    path('area_Create/',views.AreaCreateView.as_view(), name='area_Create'),
    path('area_Update/<int:pk>/',views.AreaUpdateView.as_view(), name='area_Update'),
    path('area_Delete/<int:pk>/',views.AreaDeleteView.as_view(),name='area_Delete'),
#----------------------------------------------Skill URLS------------------------------------------------------------
    path('skill_List/', views.SkillListView.as_view(), name='skill_List'),
    path('skill_Detail/<int:pk>/', views.SkillDetailView.as_view(), name='skill_Detail'),
    path('skill_Create/',views.SkillCreateView.as_view(), name='skill_Create'),
    path('skill_Update/<int:pk>/',views.SkillUpdateView.as_view(), name='skill_Update'),
    path('skill_Delete/<int:pk>/',views.SkillDeleteView.as_view(),name='skill_Delete'),
#----------------------------------------------Difficulty URLS------------------------------------------------------
    path('difficulty_List/', views.DifficultyListView.as_view(), name='difficulty_List'),
    path('difficulty_Detail/<int:pk>/', views.DifficultyDetailView.as_view(), name='difficulty_Detail'),
    path('difficulty_Create/',views.DifficultyCreateView.as_view(), name='difficulty_Create'),
    path('difficulty_Update/<int:pk>/',views.DifficultyUpdateView.as_view(), name='difficulty_Update'),
    path('difficulty_Delete/<int:pk>/',views.DifficultyDeleteView.as_view(),name='difficulty_Delete'),
]
