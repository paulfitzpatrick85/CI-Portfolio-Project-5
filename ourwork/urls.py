from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ourwork.views import projects_list


urlpatterns = [
    path('projects.html', views.projects_list, name='projects_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

