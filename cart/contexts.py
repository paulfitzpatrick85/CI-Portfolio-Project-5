from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from package.models import Package


def cart_contents(request):

    cart_items = []
    total = 0
# not used, but left if for future use on expanding website
    package_count = 0  
    cart = request.session.get('cart', {})

#  Not used - left in project for future adjustments to site after course
    for item_id, quantity in cart.items():
        package = get_object_or_404(Package, pk=item_id)
        total += quantity * package.price
        package_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'package': package,
        })

    tax = ((total / 100) * 23)
    grand_total = total + tax
    
    context = {
        'cart_items': cart_items,
        'tax': tax,
        'total': total,
        'package_count': package_count,
        'grand_total': grand_total,
    }

    return context