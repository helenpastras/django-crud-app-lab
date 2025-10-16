from django.db import models
from django.urls import reverse

# Create your models here.
class Card(models.Model):
    brandName = models.CharField(max_length=100)
    seriesName = models.CharField(max_length=100)
    characterName  = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    releaseYear = models.DateField()
    category = models.ImageField()

    def __str__(self):
        return self.name

    # Define a method to get the URL for this particular cat instance
