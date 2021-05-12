from django import forms
from .models import Videojuego

class VideojuegoForm(forms.ModelForm):

    class Meta:
        model = Videojuego

        fields = '__all__'

QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CarritoCantidadForm(forms.Form):
    cantidad = forms.TypedChoiceField(choices=QUANTITY_CHOICES,
                                      coerce=int)
