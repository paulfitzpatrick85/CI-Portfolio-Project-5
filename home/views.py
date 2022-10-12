from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Subscribe
from .forms import SubscribeForm
from django.contrib import messages


def index(request):
    """ A view to return the index page """

    return render(request, 'index.html')


# subscribe and message form
def subscribe_form(request):
    form = SubscribeForm(request.POST)

    if request.method == "POST":
        form = SubscribeForm(request.POST)  # populate form in django with request.POST data instead of doing it manually
        if form.is_valid():    # is_valid= django compare data in post request to data required on model
            form.instance.email = request.user.email
            form.instance.name = request.user.username
            subform = form.save(commit=False)
            subform.save()        # see commits for original code
            messages.success(request, 
            'Thank your for reviewing our service, your review will be displayed shortly.')
        else:
            form = SubscribeForm()

        return redirect('subscribe.html')  # directed here after adding review
    form = SubscribeForm()
    context = {
        'form': form, 'sub_added': True,
    }
    return render(request, 'subscribe.html', context)