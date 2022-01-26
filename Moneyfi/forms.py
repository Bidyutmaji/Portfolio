from re import I
from django.forms import ModelForm, TextInput
from httpx import request
# from httpx import request
from matplotlib import widgets
from Moneyfi.models import MoneyfiModel

class MoneyfiForm(ModelForm):
    class Meta:
        model = MoneyfiModel
        fields = ['mf_name', 'mf_units', 'mobile']
        widgets = {
            'mf_name': TextInput(attrs={'class':'form-control', 'placeholder':'Enter Fund Name'}),
            'mf_units': TextInput(attrs={'class':'form-control', 'placeholder':'Enter Fund Units'}),
            'mobile': TextInput(attrs={'class':'form-control', 'placeholder':'Enter Mobile Number', 'maxlenght':'10', 'readonly':'readonly'})
        }