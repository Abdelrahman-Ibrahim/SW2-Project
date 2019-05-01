from django import forms
from .models import AllData


class Form(forms.ModelForm):
    class Meta:
        model= AllData
        fields= [ "title" , "data" ]

