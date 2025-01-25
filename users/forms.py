from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)  # Corrected the tuple syntax

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):  # Corrected inheritance here                  
        model = CustomUser
        fields = UserChangeForm.Meta.fields
