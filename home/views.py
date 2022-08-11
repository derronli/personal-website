from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    #Filters class and keeps the featured projects
    featured_projects = Project.objects.filter(featured=True)[0:2]
    context = {'projects':featured_projects}

    return render(request, 'home/home_page.html', context)

def projects(request):
    #All projects
    projects = Project.objects.all()

    context = {'projects':projects}
    return render(request, 'home/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)

    context = {'project':project}
    return render(request, 'home/project.html', context)

def contact(request):
    return render(request, 'home/contact.html')