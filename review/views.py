from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Review
from .forms import ReviewForm
from django.contrib import messages


def reviews_list(request):
    reviews = Review.objects.all()  # query set of all reviews in the db
    context = {        # dict with reviews
        'reviews': reviews
    }

    return render(request, 'reviews.html', context)  #  add context as arg so can be accessed in review.html template


def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)  # populate form in django with request.POST data instead of doing it manually
        if form.is_valid():   # is_valid= django compare data in post request to data required on model
            form.save()        # see commits for original code

        return redirect('reviews.html')  # directed here after adding review
    form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'add_review.html', context)