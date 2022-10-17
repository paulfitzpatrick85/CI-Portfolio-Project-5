from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('packages.html', views.all_packages, name='all_packages'),
    path('package_detail.html/<package_id>/', views.package_detail, name='package_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)