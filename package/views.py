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


def package_detail(request, package_id):
    """ A view to return the package details page """
    package = get_object_or_404(Package, pk=package_id)
    context = {
        'package': package,
    }

    return render(request, 'package_detail.html', context)
