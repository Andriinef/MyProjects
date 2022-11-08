from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]
