from django import forms
from .models import UserProfile, ROLE_CHOICES
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate



class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Role')

    class Meta:
        model = UserProfile
        fields = ['telegram', 'first_name', 'last_name', 'password', 'password_confirm', 'role']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        telegram = cleaned_data.get('telegram')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        if telegram and UserProfile.objects.filter(telegram=telegram).exists():
            raise forms.ValidationError("Telegram username already in use.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Use set_password for hashing
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    telegram = forms.CharField(label="Telegram Username", max_length=254)
    def clean(self):
        telegram = self.cleaned_data.get('telegram')
        password = self.cleaned_data.get('password')

        if telegram and password:
                # Authenticate using telegram as the username
            self.user_cache = authenticate(self.request, username=telegram, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                        "Invalid Telegram ID or password.",
                        code='invalid_login'
                    )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data