from django.forms import ModelForm, TextInput

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