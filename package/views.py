from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Package
from django.contrib import messages

# Create your views here.


def all_packages(request):
    """ A view to return the packages page """

    packages = Package.objects.all

    context = {
        'packages': packages,
    }

    return render(request, 'packages.html', context)