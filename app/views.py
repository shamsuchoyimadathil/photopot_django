from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 

from . import models
from . import forms

# Create your views here.
class MainPage(ListView):
    template_name = "app/main.html"
    model = models.Upload
    queryset = models.Upload.objects.all()
    context_object_name = "mainPage"


class UploadPage(FormView):
    login_required = True
    template_name = "app/upload.html"
    success_url= "/main"
    form_class = forms.UploadForm

    def post(self, request):

        form = forms.UploadForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

        return render(request,"app/upload.html",{
            "form":form
        })


class DetailImage(DetailView):
    template_name = "app/detail.html"
    model = models.Upload
    context_object_name = "detailPage"


class Favorites(ListView):
    template_name = "app/favorite.html"
    model = models.Upload

    def get(self,request):
        favorite_images = request.session.get("favorite_images")

        context = {}

        if favorite_images is None or len(favorite_images) == 0:
            context["images"] = []
            context["has_images"] = False

        else:
            images = models.Upload.objects.filter(id__in=favorite_images)
            context["images"] = images
            context["has_images"] = True

        return render(request, "app/favorite.html",context)

    def post(self,request):
        favorite_images = request.session.get("favorite_images")
        if favorite_images is None:
            favorite_images = []

        favorite_id = int(request.POST["favorite_id"])

        if 'add' in request.POST:
            if favorite_id not in favorite_images:
                favorite_images.append(favorite_id)

        elif 'remove' in request.POST:
            if favorite_id in favorite_images:
                favorite_images.remove(favorite_id)

        request.session["favorite_images"] = favorite_images
        

        return HttpResponseRedirect("/")
