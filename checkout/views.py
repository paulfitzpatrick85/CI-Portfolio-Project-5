from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import PackageOrderedForm
from package.models import Package
from .models import Package_ordered, OrderLineItem  
from cart.contexts import cart_contents
from django.conf import settings
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Your payment cannot be \
            processed.')
        return HttpResponse(content=e, status=400)

    
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY  

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'customer_name': request.POST['customer_name'],
            'customer_email': request.POST['customer_email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
        }
        order_form = PackageOrderedForm(form_data)
        if order_form.is_valid():
            package_order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            Package_ordered.stripe_pid = pid
            Package_ordered.original_cart = json.dumps(cart)
            package_order.save()
            for item_id, item_data in cart.items():
                try:
                    package = Package.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            package_order=package_order,
                            package=package,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        order_line_item.save()
                except Package.DoesNotExist:
                    messages.error(request, (
                        "One of the packages in your cart \
                         wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    package_order.delete()
                    return redirect(reverse('view_cart'))

            # request.session['save_info'] = 'save-info' in request.POST #uncommented 10/12 so may need deleting
            return redirect(reverse('checkout_success',
                            args=[package_order.order_number]))
        else:
        
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in \
                                     your cart at the moment")
            return redirect(reverse('all_packages'))

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty" "Return to the \
                                 Product Packages page to add to your cart")
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


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    package_order = get_object_or_404(Package_ordered, 
                                      order_number=order_number)
    # _send_confirmation_email(package_order)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. We will \
        be in touch soon to discuss your new site!')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout_success.html'
    context = {
        'package_order': package_order,
    }