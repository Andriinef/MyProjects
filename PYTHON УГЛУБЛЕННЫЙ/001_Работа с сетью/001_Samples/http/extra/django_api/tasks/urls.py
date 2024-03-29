from django.contrib import admin
from django.urls import include, path
from issues.views import AuthView, IssueModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("issues", IssueModelViewSet, base_name="issues")
router.register("auth", AuthView, base_name="auth")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.get_urls())),
]
