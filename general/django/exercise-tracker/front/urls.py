from django.urls import path
from .views import exercise_tracker_index

urlpatterns = [path("", exercise_tracker_index, name="index")]
