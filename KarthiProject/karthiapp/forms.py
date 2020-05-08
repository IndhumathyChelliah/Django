from django import forms
from karthiapp.models import KarthiData

class FormName(forms.ModelForm):
    class Meta:
        model=KarthiData
        fields="__all__"