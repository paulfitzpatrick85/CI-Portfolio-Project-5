from django.http import HttpResponse
from .models import OrderLineItem, Package_ordered
from django.core.mail import send_mail
from django.template.loader import render_to_string
from package.models import Package
import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = package_ordered.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'package_ordered': package_ordered})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'package_ordered': package_ordered, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )        

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details  # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)  # updated

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        package_order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                # print(billing_details)
                order = Package_ordered.objects.get(
                    customer_name__iexact=billing_details.name,
                    customer_email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    postcode__iexact=shipping_details.address.postal_code,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                package_order_exists = True
                break
            except Package_ordered.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if package_order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Order Already In DataBase',
                status=200)
        else:
            order = None
            try:
                order = Package_ordered.objects.create(
                    customer_name__iexact=billing_details.name,
                    customer_email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    postcode__iexact=shipping_details.address.postal_code,
                    original_cart=cart,
                    stripe_pid=pid,
                    )
                for item_id, item_data in json(cart).items():
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)