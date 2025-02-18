from django.urls import path
from . import views

urlpatterns = [
    path('hero/', views.HeroList.as_view(), name='hero-list'),
    path('about/', views.AboutList.as_view(), name='about-list'),
    path('resume/', views.ResumeList.as_view(), name='resume-list'),
    path('skills/', views.SkillsList.as_view(), name='skills-list'),
    path('projects/', views.ProjectsList.as_view(), name='projects-list'),
    path('send-message/', views.SendMessage.as_view(), name='send-message'),
] 