from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('avatar', 'contact')

class PerfomancerForm(forms.ModelForm):
    class Meta:
        model = Performer
        fields = ('avatar', 'contact')
