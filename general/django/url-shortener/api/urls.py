from django.urls import path
from .views import UrlShortenerView

urlpatterns = [
    path("shorturl", UrlShortenerView.as_view(), name="shorturl"),
    path("shorturl/<short_url>", UrlShortenerView.as_view(), name="shorturl"),
]
