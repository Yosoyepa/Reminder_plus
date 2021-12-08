from django import forms
from django.forms import ModelForm, fields
from . models import Notes

class NotesForm(ModelForm):
    heading = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder":"Ingresa El Titulo"
    }))
    text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
         "class": "form-control", "placeholder":"Ingresa Tu Nota", "rows":"8"
    }))
    class Meta:
        model = Notes
        fields = ['heading', 'text']