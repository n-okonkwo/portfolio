from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/kamtek/', views.project_detail, name='project_detail'),
]