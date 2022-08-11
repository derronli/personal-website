from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-home'),
    path('projects/', views.projects, name='home-projects'),
    path('project/<str:pk>/', views.project, name='home-project'),
    path('contact/', views.contact, name='home-contact'),
]