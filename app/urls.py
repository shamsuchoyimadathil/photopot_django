from django.urls import path
from . import views

urlpatterns = [
    path("",views.MainPage.as_view(),name="main-page"),
    path("login",views.LoginPage.as_view(),name="login-page"),
    path("upload",views.UploadPage.as_view(),name="upload-page"),
    path("detail",views.DetailImage.as_view(),name="detail-page"),
    path("favorite",views.Favorites.as_view(),name="favorite-page"),

]
