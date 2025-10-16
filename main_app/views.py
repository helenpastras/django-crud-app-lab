from django.shortcuts import render, redirect
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card

# Create your views here.

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def card_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})


def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'cards/detail.html', {'card': card})


# CRUD
class CardCreate(CreateView):
    model = Card
    fields='__all__'


class CardUpdate(UpdateView):
    model = Card
    fields='__all__'


class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'

