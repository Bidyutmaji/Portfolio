from django import forms

class ImageSearch(forms.Form):
    search = forms.CharField(max_length=50)
    num_image = forms.IntegerField(max_value=25, required=False)
    quality = forms.ChoiceField(choices=(
        ('raw', '4k'),
        ('full', 'Full HD'),
        ('regular', "HD")
    ))