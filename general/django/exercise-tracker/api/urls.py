from django.urls import path
from .views import users, logs, exercises

urlpatterns = [
    path("users", users, name="users"),
    path("users/<int:username_id>/logs", logs, name="logs"),
    path("users/<int:username_id>/exercises", exercises, name="exercises"),
]
