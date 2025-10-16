from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    CATEGORY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('super-rare', 'Super Rare'),
        ('ultra-rare', 'Ultra Rare'),
        ('die-cast-rare', 'Die-Cast Rare'),
        ('parallels', 'Parallels'),
        ('refractor', 'Refractor'),
        ('autograph', 'Autograph'),
        ('dual-autograph', 'Dual Autograph'),
        ('signature', 'Signature'),
    ]

    brandName = models.CharField(max_length=100)
    seriesName = models.CharField(max_length=100)
    characterName = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True)
    releaseYear = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    cardImage = models.ImageField(upload_to='card_images/', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.characterName} ({self.seriesName})"
    