from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('wordle/', views.wordle, name = 'blog-wordle'),
    path('project/', views.projects, name='blog-projects')
]