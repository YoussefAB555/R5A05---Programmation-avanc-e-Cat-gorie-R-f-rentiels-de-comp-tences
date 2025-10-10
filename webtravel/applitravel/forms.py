from django import forms
from django.forms import ModelForm
from .models import Ville, Voyage

class VilleForm(ModelForm):
    class Meta:
        model = Ville
        fields = ['NomVille','NomPays']
        labels ={
            'NomVille':'Nom de la ville',
            'NomPays':'Nom du Pays',
        }

class VoyageForm(ModelForm):
    class Meta:
        model = Voyage
        fields = ['Titre','Prix']