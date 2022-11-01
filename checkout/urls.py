from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('checkout.html', views.checkout, name='checkout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

