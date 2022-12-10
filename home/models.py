from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Subscribe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    # this is for admin to track who they have replied to or not
    message_replied_to = models.BooleanField(default=False)

    def __str__(self):
        return self.name