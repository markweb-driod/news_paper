from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class Signup(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')  # Ensure 'home' exists in urls.py
    template_name = 'registration/signup.html'