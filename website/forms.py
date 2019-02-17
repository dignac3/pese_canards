from django import forms

from website.models import Pesee, Poids


class PeseeForm(forms.ModelForm):

    class Meta:
        model = Pesee
        fields = ['semaine','poids_min','poids_max','tare']


class PoidsForm(forms.ModelForm):
    class Meta:
        model = Poids
        fields = ['poids']