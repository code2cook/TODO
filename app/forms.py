from django.forms import ModelForm
from django import forms


from app.models import TODO
class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title' , 'status' , 'priority']
    
        
class PictureUploadForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    picture = forms.FileField()