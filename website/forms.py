from django import forms

from website.models import Pesee


class PeseeForm(forms.ModelForm):

    class Meta:
        model = Pesee
        fields = ['semaine','poids_min','poids_max','tare']


