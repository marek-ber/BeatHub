from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]


User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Adres email")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
        labels = {
            "username": "Nazwa użytkownika",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].help_text = (
            "Maksymalnie 150 znaków."
        )

        self.fields["password1"].label = "Hasło"
        self.fields["password2"].label = "Powtórz hasło"

        self.fields["password1"].help_text = (
            "Hasło musi mieć minimum 8 znaków."
        )

        self.fields["password2"].help_text = (
            "Wpisz ponownie hasło."
        )