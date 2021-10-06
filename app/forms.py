from django import forms
from . import models

class UploadForm(forms.ModelForm):
    class Meta:
        model = models.Upload 
        fields =  "__all__" 

    def __init__(self,*args, **kwargs):
        super(UploadForm,self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs=({'placeholder':'what title do you want to give it ?'})