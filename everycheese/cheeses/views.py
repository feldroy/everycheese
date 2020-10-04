
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from .models import Cheese


class CheeseListView(ListView):
    model = Cheese


class CheeseDetailView(DetailView):
    model = Cheese


class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country_of_origin']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class CheeseUpdateView(LoginRequiredMixin, UpdateView):
    model = Cheese
    fields = {
        'name',
        'description',
        'firmness',
        'country_of_origin'
    }
    action = 'Update'