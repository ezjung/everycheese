from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Cheese


class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model=Cheese