from django.urls import path
from .views import WhoamiView

urlpatterns = [path("whoami", WhoamiView.as_view(), name="whoami")]
