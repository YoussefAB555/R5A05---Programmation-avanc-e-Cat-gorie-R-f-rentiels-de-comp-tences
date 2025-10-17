from django import forms
from django.contrib.auth.models import User
from .models import TravelUser

class TravelUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class TravelUserImageForm(forms.ModelForm):
    class Meta:
        model = TravelUser
        fields = ('image',)