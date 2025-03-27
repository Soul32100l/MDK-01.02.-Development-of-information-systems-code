from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ("username", "email", "password1", "password2")



        def save(self, commit=True):
            CustomUser = super().save(commit=False)
            CustomUser.email = self.cleaned_data["email"]
            if commit:
                CustomUser.save()
            return CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )

    error_messages = {
        'invalid_login': "Неверные учетные данные",
        'inactive': "Аккаунт неактивен",
    }

