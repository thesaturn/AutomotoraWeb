from django import forms

from .models import Auto

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = [
        'marca',
        'modelo',
        'año',
        'color',
        'númeropuertas',
        'descripcion',
        'fechapublicación',
        'precio'
        ]
