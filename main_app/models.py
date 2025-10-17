from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Card(models.Model):
    CATEGORY_CHOICES = [
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Super-Rare', 'Super Rare'),
        ('Ultra-Rare', 'Ultra Rare'),
        ('Die-Cast-Rare', 'Die-Cast Rare'),
        ('Parallels', 'Parallels'),
        ('Refractor', 'Refractor'),
        ('Autograph', 'Autograph'),
        ('Dual-Autograph', 'Dual Autograph'),
        ('Signature', 'Signature'),
    ]

    brandName = models.CharField(max_length=100)
    seriesName = models.CharField(max_length=100)
    characterName = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True)
    releaseYear = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.characterName} ({self.seriesName})"
    
    def get_absolute_url(self):
        return reverse('card-detail', kwargs={'card_id' : self.id})
    

class CardImage(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='card_images/')

    def __str__(self):
        return f"Image for {self.card.characterName}"