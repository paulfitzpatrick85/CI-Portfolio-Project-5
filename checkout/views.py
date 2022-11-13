from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PackageOrderedForm
from cart.contexts import cart_contents
from django.conf import settings
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty" "Return to the Product Packages page to add to your cart")
        return redirect(reverse('packages'))

    current_cart = cart_contents(request) 
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    package_ordered_form = PackageOrderedForm()
# below may be deleted later
    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing. '
                                   'Did you forget to set it in '
                                   'your environment?'))

    template = 'checkout.html'
    context = {
        'package_ordered_form': package_ordered_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)