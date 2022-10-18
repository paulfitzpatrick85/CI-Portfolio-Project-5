from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
# from .models import Package
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """ A view to return the cart contents page """

    return render(request, 'cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):           # might/will be delete later
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)