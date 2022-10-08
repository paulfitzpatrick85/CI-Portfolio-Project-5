from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Projects(models.Model):
    project_title = models.CharField(max_length=80)
    project_description = models.TextField()
    project_image = models.ImageField(blank=True, upload_to='media/')
    project_url = models.URLField(max_length=100)
    project_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.project_title