from django.urls import path

from .views import ResultView, UploadView

app_name = "textprocessor"

urlpatterns = [
    path("", UploadView.as_view(), name="upload"),
    path("result/", ResultView.as_view(), name="result"),
]
