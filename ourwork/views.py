from django.shortcuts import render

def projects(request):
    """ A view to return the project's' page page """

    return render(request, 'projects.html')
