from django.shortcuts import render, redirect

# Create your views here.

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    # return HttpResponse('<h1>Hello 🅒ᗋℝᑔ 🄒Ⓞ🅛🅛𝔼🄒ẗ𝕆🅁! ')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def card_index(request):
#     cards = Card.objects.all()
#     return render(request, 'cards/index.html', {'cards': cards})
