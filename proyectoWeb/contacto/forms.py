from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='nombre', required=True, max_length=100)
    email = forms.EmailField(label='email', required=True)
    descripcion = forms.CharField(label='descripcion', widget=forms.Textarea)
