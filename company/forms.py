from django import forms
from . import models


class Contactform(forms.ModelForm):
    class Meta:
        model = models.Contactus
        fields = ['fullname', 'email',  'description']

        widgets = {
            'fullname': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'cf-name', 'name': 'name', 'placeholder': 'Name'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'email', 'id': 'cf-name', 'placeholder': 'Email',
                       'name': 'name'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '6', 'id': 'cf-name', 'placeholder': 'Message',
                       'name': 'name'}),
        }
