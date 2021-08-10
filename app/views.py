from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from django.views.generic import CreateView

from . import models
from . import forms

# Create your views here.
class MainPage(ListView):
    template_name = "app/main.html"
    model = models.Upload
    queryset = models.Upload.objects.all()
    context_object_name = "mainPage"

class LoginPage(LoginView):
    template_name = "app/login.html"
    #success_url = "/main"

class UploadPage(FormView):
    template_name = "app/upload.html"
    success_url= "/main"
    form_class = forms.UploadForm

class DetailImage(DetailView):
    template_name = "app/detail.html"
    model = models.Upload

class Favorites(ListView):
    template_name = "app/favorite.html"
    #model 

class SignUP(FormView):
    template_name = "app/signup.html"
    form_class = forms.SignUpForm
    success_url = "/login"
    