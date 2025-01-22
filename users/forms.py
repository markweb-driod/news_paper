from django import forms
from django.contrib.auth import UserCreationForms, UserChangeForm
from .models import CustomUser

class Createcustomuser(UserCreationForms):
    class Meta(UserCreationForms.Meta):
        model = CustomUser
        fields = UserCreationForms.Meta.Fields + ('age')