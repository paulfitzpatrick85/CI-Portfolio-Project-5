from django.contrib import admin
from .models import Projects
# Register your models here.

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    search_fields = ('project_title', 'project_url')
    actions = ['approve_project']
    list_display = ('project_title', 'project_approved')

    def approve_project(self, request, queryset):
        queryset.update(approved=True)

    