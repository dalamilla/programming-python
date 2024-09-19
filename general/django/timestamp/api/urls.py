from django.urls import path
from .views import DateView

urlpatterns = [
    path("", DateView.as_view(), name="date"),
    path("<str:input_date>", DateView.as_view(), name="date"),
]
