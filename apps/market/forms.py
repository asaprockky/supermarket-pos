from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from . import models

class MarketLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('username')

        if username and password:
            self.user_cache = authenticate(self.request, username, password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Invalid Telegram ID or password.",
                    code='invalid_login'
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
    

class AddProductFOrm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields  = ["product_name", "stock", "barcode", "price", "cost", "description"]