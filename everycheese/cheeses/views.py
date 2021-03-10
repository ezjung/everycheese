from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render


from .models import Cheese


class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model=Cheese

class CheeseCreateView(CreateView):
    model=Cheese
    fields = [
        'name',
        'description',
        'firmness',
        'country_of_origin'
    ]