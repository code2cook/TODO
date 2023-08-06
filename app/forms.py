from django.forms import ModelForm
from django import forms

    
        
class PictureUploadForm(forms.Form):
    foodName = forms.CharField(max_length=100)
    conmon = forms.CharField(widget=forms.Textarea)
    picture = forms.FileField()