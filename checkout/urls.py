from . import views
from django.urls import path
from django.conf import settings        
from django.conf.urls.static import static  

urlpatterns = [
    path('checkout.html', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', 
         views.checkout_success, name='checkout_success'),
    path('checkout/cache_checkout_data/', 
         views.cache_checkout_data, name='cache_checkout_data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)