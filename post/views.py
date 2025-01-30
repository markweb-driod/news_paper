from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationForm
# Create your views here.
class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home.html')
    template_name = 'registration/signup.html'