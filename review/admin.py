from django.contrib import admin
from .models import Review
# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('customer_name', 'customer_email', 'customer_review')
    actions = ['approve_review']
    list_display = ('customer_name', 'review_approved')

    def approve_review(self, request, queryset):
        queryset.update(approved=True)
