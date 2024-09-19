from django.urls import path
from .views import file_metadata_index

urlpatterns = [path("", file_metadata_index, name="index")]
