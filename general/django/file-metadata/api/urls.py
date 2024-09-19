from django.urls import path
from .views import FileUploadView

urlpatterns = [path("fileanalyse", FileUploadView.as_view(), name="fileanalyse")]
