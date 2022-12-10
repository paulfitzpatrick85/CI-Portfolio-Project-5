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
        form = SubscribeForm(request.POST)
        if form.is_valid():           
            form.instance.email = request.user.email
            form.instance.name = request.user.username
            subform = form.save(commit=False)
            subform.save()
            messages.success(request, 'Thank you for contacting us,\
             we will respond as soon as possible.')
        else:
            form = SubscribeForm()

        return redirect('subscribe.html')
    form = SubscribeForm()
    context = {
        'form': form, 'sub_added': True,
    }
    return render(request, 'subscribe.html', context)