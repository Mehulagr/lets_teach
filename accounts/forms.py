from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import Account

class RegistrationForm(ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Account
        exclude = ('user',)

    def clean_username(self):
        username =self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, please select another")

    def clean(self):
        password = self.cleaned_data["password"]
        password1 = self.cleaned_data["password1"]
        if password != password1:
            raise forms.ValidationError("The Passwords did not match. Please try again")
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label=(u"User Name"))
    password = forms.CharField(label=(u"Password"), widget=forms.PasswordInput(render_value=False))

