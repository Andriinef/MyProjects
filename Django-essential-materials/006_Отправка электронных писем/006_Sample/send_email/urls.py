from django.contrib import admin
from django.contrib.auth import views as auth
from django.urls import include, path

from .views import activate_account, subscription, usersignup

urlpatterns = [
    path("logout/", auth.LogoutView.as_view(template_name="index.html"), name="logout"),
    path(r"signup/", usersignup, name="register_user"),
    path(r"activate/<uidb64>/<token>/", activate_account, name="activate"),
    path("subscription/", subscription, name="subscription"),
]
