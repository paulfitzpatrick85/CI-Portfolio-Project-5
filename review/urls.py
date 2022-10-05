from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from review.views import reviews_list


urlpatterns = [
    path('reviews.html', views.reviews_list, name='reviews_list'),
]