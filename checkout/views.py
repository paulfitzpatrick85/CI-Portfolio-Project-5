from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PackageOrderedForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty" "Return to the Product Packages page to add to your cart")
        return redirect(reverse('packages'))

    package_ordered_form = PackageOrderedForm()
    template = 'checkout/checkout.html'
    context = {
        'package_ordered_form': package_ordered_form,
    }

    return render(request, template, context)