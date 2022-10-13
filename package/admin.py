from django.contrib import admin
from .models import Package
# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'price', 'image', )
    ordering = ('name',)



