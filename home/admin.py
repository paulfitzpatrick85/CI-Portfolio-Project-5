from django.contrib import admin
from .models import Subscribe
# Register your models here.


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'message')
    actions = ['message_replied_to']
    list_display = ('name', 'message_replied_to')

    def message_replied_to(self, request, queryset):
        queryset.update(approved=True)