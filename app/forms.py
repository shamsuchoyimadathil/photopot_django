from django import forms
#from django.contrib.auth import forms
from django.core.exceptions import ValidationError
from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.SignUp
        widgets = {
            'password':forms.PasswordInput(),
            'confirm_password':forms.PasswordInput(),
            'DOB':forms.SelectDateWidget(),
        }
        fields = "__all__"

    def clean_form(self):
        cleaned_data = super(self,SignUpForm).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise ValidationError (
                'the password confirmation does not match'
            )

        