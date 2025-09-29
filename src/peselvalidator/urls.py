from django.urls import path

from .views import PeselFormView

app_name = "peselvalidator"

urlpatterns = [
    path("", PeselFormView.as_view(), name="form"),
]
