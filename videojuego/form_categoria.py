from django import forms
from .models import Categoria, Videojuego

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = '__all__'

class  VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego

        fields = '__all__'

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'anio':forms.NumberInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'precio':forms.NumberInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control','rows':'60'})
        }