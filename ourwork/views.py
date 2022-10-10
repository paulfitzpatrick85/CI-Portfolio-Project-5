from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Projects
from django.contrib import messages


def projects_list(request):
    """ A view to return the project's' page page """
    paginate_by = 8
    projects = Projects.objects.filter(project_approved=True)
    context = {        # dict with reviews
        'projects': projects
    }

    return render(request, 'projects.html', context)


