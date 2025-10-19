from django import forms
from django.forms import modelformset_factory
from .models import CardImage

CardImageFormSet = modelformset_factory(CardImage, fields=('image',), extra=1)

class CardImageForm(forms.ModelForm):
    class Meta:
        model = CardImage
        fields = ['image']

