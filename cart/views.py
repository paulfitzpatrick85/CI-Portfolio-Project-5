from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import generic, View
from django.contrib import messages
from package.models import Package
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.


def view_cart(request):
    """ A view to return the cart contents page """

    return render(request, 'cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the cart """  
    package = Package.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):           
        messages.success(request, f'{package.name} is already in your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'{package.name} \
        has been added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


@csrf_exempt
def remove_from_cart(request, item_id):
    """Remove the item from the cart"""

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

