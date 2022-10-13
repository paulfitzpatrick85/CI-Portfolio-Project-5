from django.db import models


# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=254)
    short_description = models.TextField(default='description')
    full_description = models.TextField(default='description')
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name   # returns product name