from django import forms
from django.forms import ModelForm
from users.models import FarmMap, User

from leaflet.forms.widgets import LeafletWidget


class FarmMapForm(forms.ModelForm):

    class Meta:
        model = FarmMap
        fields = ('name', 'geom')
        widgets = {'geom': LeafletWidget()}
