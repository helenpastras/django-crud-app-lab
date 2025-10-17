from django import forms
from .models import CardImage

class CardImageForm(forms.ModelForm):
    class Meta:
        model = CardImage
        fields = ['image']