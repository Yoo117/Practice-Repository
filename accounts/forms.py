from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'nickname', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

    class Meta:
        model = User
        fields = ['email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'email']

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
