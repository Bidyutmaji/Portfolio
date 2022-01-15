from django import forms
from django import forms

class ImageSearch(forms.Form):
    search = forms.CharField(max_length='50')