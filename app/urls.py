from django.urls import path
from . import views

urlpatterns = [
    path("",views.MainPage.as_view(),name="main-page"),
    #path("login",views.LoginPage.as_view(),name="login-page"),
    path("login",views.loginpage , name="login-page"),
    path("signup",views.SignUP.as_view(),name="signup-page"),
    path("upload",views.UploadPage.as_view(),name="upload-page"),
    path("detail/<slug:pk>",views.DetailImage.as_view(),name="detail-page"),
    path("favorite",views.Favorites.as_view(),name="favorite-page"),
]
