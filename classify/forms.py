from django import forms

class ImageFileForm(forms.Form):
    file = forms.FileField()
                            
class ContactForm(forms.Form):
    mail = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control','id':"email",'placeholder':'Email'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control','id':"subject",'placeholder':'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','id':"subject",'placeholder':'Enter your message'}))

