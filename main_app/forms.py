from django import forms
from django.forms import modelformset_factory
from .models import CardImage, Card

CardImageFormSet = modelformset_factory(CardImage, fields=('image',), extra=1)

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'  
        exclude = ['owner']

class CardImageForm(forms.ModelForm):
    class Meta:
        model = CardImage
        fields = ['image']