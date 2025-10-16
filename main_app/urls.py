
from django.contrib import admin
from django.urls import path, include

from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.card_index, name='card-index'),
    path('cards/<int:card_id>/', views.card_detail, name='card-detail'),
]
