from django import forms
#from django.contrib.auth import forms
from django.core.exceptions import ValidationError
from django.forms import fields, widgets
from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.SignUp
        widgets = {
            'password':forms.PasswordInput(),
            'confirm_password':forms.PasswordInput(),
            'DOB':forms.SelectDateWidget(years=range(1900, 2100)),
        }
        fields = "__all__"

    def clean(self):
        cleaned_data = super(SignUpForm,self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            print("clean form is working")
            raise ValidationError (
                'the password confirmation does not match'
            ) 
        



    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs=({'class':'form-control','placeholder':'your username'})
        self.fields['password'].widget.attrs=({'class':'form-control','placeholder':'your password'})
        self.fields['confirm_password'].widget.attrs=({'class':'form-control','placeholder':'confirm password'})
        self.fields['DOB'].widget.attrs=({'min':'1980-01-01','max':'2050-12-31'})
        



class UploadForm(forms.ModelForm):
    class Meta:
        model = models.Upload 
        fields =  "__all__"