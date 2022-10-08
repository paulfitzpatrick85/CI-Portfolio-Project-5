from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ourwork.views import projects


urlpatterns = [
    path('project.html', views.projects, name='projects'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)