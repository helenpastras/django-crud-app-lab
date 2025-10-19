from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import modelformset_factory
from .models import Card, CardImage
from .forms import CardForm, CardImageForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

CardImageFormSet = modelformset_factory(CardImage, fields=('image',), extra=1)

# Define the home view function
class Home(LoginView):
    template_name = 'home.html'

            
def about(request):
    return render(request, 'about.html')

@login_required
def card_index(request):
    cards = Card.objects.filter(owner=request.user)
    return render(request, 'cards/index.html', {'cards': cards})

@login_required
def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    images = card.images.all()  # thanks to related_name
    return render(request, 'cards/detail.html', {'card': card, 'images': images})

@login_required
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


# CRUD
class CardCreate(CreateView):
    model = Card
    form_class = CardForm
    template_name = 'cards/card_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['image_formset'] = CardImageFormSet(self.request.POST, self.request.FILES, queryset=CardImage.objects.none())
        else:
            context['image_formset'] = CardImageFormSet(queryset=CardImage.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']
        form.instance.owner = self.request.user
        self.object = form.save()
        if image_formset.is_valid():
            for image_form in image_formset:
                if image_form.cleaned_data:
                    image = image_form.save(commit=False)
                    image.card = self.object
                    image.save()
        return super().form_valid(form)

class CardUpdate(LoginRequiredMixin,UpdateView):
    model = Card
    fields='__all__'


class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'

