from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']
        labels = {
            'nombre': 'Nombre',
            'email': 'Email',
            'mensaje': 'Mensaje',
        }