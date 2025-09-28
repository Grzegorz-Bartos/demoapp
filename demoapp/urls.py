from django.contrib import admin
from django.urls import include, path

from textprocessor.views import UploadView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("text/", include("textprocessor.urls")),
    path("pesel/", include("peselvalidator.urls")),
    path("", UploadView.as_view(), name="home"),
]
