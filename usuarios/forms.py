from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario

        fields = ('first_name','username','password','email','estado','municipio','foto')

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
            'municipio':forms.Select(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'})
        }

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UsuarioActualizarForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = ('first_name','username','email','estado','municipio','foto')

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
            'municipio':forms.Select(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'})
        }

class UsuarioRegistroForm(forms.ModelForm):

    class Meta:
        model = Usuario
        
        fields = ('username','password','email','estado','municipio')

        widgets = {
            'estado':forms.Select(attrs={'class':'form-control'}),
            'municipio':forms.Select(attrs={'class':'form-control'}),
        }

    def save(self, commit=True):
        user = super(UsuarioRegistroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
