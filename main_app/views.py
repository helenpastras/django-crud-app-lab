from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card
from .forms import CardImageForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm



# Define the home view function
class Home(LoginView):
    template_name = 'home.html'

            
def about(request):
    return render(request, 'about.html')

def card_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})


def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    images = card.images.all()  # thanks to related_name
    return render(request, 'cards/detail.html', {'card': card, 'images': images})


def add_card_image(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        form = CardImageForm(request.POST, request.FILES)
        if form.is_valid():
            card_image = form.save(commit=False)
            card_image.card = card
            card_image.save()
            return redirect('card-detail', card_id=card.id)
    else:
        form = CardImageForm()
    return render(request, 'cards/add_image.html', {'form': form, 'card': card})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('card-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )


# CRUD
class CardCreate(CreateView):
    model = Card
    fields='__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)


class CardUpdate(UpdateView):
    model = Card
    fields='__all__'


class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'

