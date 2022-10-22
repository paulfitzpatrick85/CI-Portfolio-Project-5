from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cart.html', views.view_cart, name='view_cart'),
    path('cart.html/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

