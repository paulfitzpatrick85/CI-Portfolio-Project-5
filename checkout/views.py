from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PackageOrderedForm
from cart.contexts import cart_contents
from django.conf import settings
import stripe


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty" "Return to the Product Packages page to add to your cart")
        return redirect(reverse('packages'))

    current_cart = cart_contents(request) 
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    package_ordered_form = PackageOrderedForm()
    template = 'checkout.html'
    context = {
        'package_ordered_form': package_ordered_form,
        'stripe_public_key': 'pk_test_51M34EZAbqy5bXrWgrA9cPJSCit8GC3AJ0dyri2te0eLwOerLdMxqsJGNa9TeHLMNo5YnOvFI4KWGIhZqZxBbk91A003zgZpHAy',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)