from django import forms

from . models import Juego, JuegoInstance

class JuegoForm(forms.ModelForm):
    title = forms.CharField(label='Title',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    desarrollador = forms.CharField(label='Desarrollador', max_length=200, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))

    genero = forms.CharField(label='Genero', max_length=200, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Juego
        fields = ('title', 'desarrollador','genero')

