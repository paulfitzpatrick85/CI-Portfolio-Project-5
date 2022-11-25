from django.contrib import admin
from .models import Package_ordered, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class Package_OrderedAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'order_tax',
                       'grand_total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'date', 'customer_name',
              'customer_email', 'phone_number',
              'order_total', 'order_tax', 'grand_total',
              'original_cart', 'stripe_pid')

    list_display = ('order_number', 'date', 'customer_name',
                    'order_total',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Package_ordered, Package_OrderedAdmin)
