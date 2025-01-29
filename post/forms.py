from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser


class Usercreationform(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)

class Userchangeform(UserChangeForm):
    class Meta:
        fields = UserChangeForm.Meta.fields
        model = CustomUser