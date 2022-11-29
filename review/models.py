from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_review = models.TextField()
    review_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.customer_name
