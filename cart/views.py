from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
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


# def remove_from_cart(request, item_id):
#     """ Remove specified product to the cart """
#     try:
#         cart.pop(item_id)
        
#         request.session['cart'] = cart
#         return HttpResponse(status=200)

#     except Exception as e:
#         return HttpResponse(status=500)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

