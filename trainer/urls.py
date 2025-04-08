from django.urls import path
from . import views
from .views import (
    TrainerListCreateView, TrainerDetailView, TrainerBySubjectView,
    SubjectListCreateView, SubjectDetailWithTrainers, SubjectDetailDeleteView
)



urlpatterns = [
     # Frontend pages
    path('', views.home, name='home'),
    path('trainers/', views.trainer_list, name='trainer-list'),
    path('trainers/add/', views.add_trainer, name='add-trainer'),
    path('subjects/', views.subject_list, name='subject-list'),
    path('subjects/add/', views.add_subject, name='add-subject'),
    path('trainers/<int:pk>/', views.view_trainer, name='view-trainer'),
    path('trainers/<int:pk>/delete/', views.delete_trainer, name='delete-trainer'),
    path('subjects/<int:pk>/', views.view_subject, name='view-subject'),
    path('subjects/<int:pk>/delete/', views.delete_subject, name='delete-subject'),
    


    
      # API endpoints
    path('trainer/', TrainerListCreateView.as_view(), name='trainer-list-create'),
    path('trainer/<int:emp_id>/', TrainerDetailView.as_view(), name='trainer-detail'),
    path('trainer/<str:subject>/topic/', TrainerBySubjectView.as_view(), name='trainer-by-subject'),
    path('subject/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subject/<int:id>/', SubjectDetailWithTrainers.as_view(), name='subject-detail'),
    path('subject/<int:pk>/delete/', SubjectDetailDeleteView.as_view(), name='subject-delete'),
]
