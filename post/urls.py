from django.urls import path
from.models import CustomUser

urlpatterns = [
    path('', signup.as_view(), name = 'signup')
]