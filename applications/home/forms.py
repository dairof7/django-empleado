from django import forms
from .models import Prueba

#  this is the mod form used in my view

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 5:
            raise forms.ValidationError('La cantidad debe ser igual o mayor a 5')
        return cantidad