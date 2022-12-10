from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from review.views import reviews_list


urlpatterns = [
    path('reviews.html', views.reviews_list, name='reviews_list'),
    path('add_review.html', views.add_review, name='add_review'),
    path('edit_review.html/<review_id>/',
         views.edit_review, name='edit_review'),
    path('delete_review.html/<review_id>/',
         views.delete_review, name='delete_review'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)