from django import forms

from backend.models import Poids


class PoidsForm(forms.ModelForm):
    class Meta:
        model = Poids
        fields = ['poids']
