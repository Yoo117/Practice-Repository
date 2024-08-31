from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from .models import User, Notification

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'nickname', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

    class Meta:
        model = User
        fields = ['email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'profile_picture']

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class NotificationForm(forms.Form):
    notification_id = forms.IntegerField(widget=forms.HiddenInput()) 

    def clean_notification_id(self):
        notification_id = self.cleaned_data['notification_id']
        if not Notification.objects.filter(id=notification_id).exists():
            raise forms.ValidationError("Invalid notification ID")
        return notification_id