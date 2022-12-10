from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('subscribe.html', views.subscribe_form, name='subscribe_form'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
