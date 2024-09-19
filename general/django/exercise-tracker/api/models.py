from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)


class Exercise(models.Model):
    description = models.TextField()
    duration = models.IntegerField()
    date = models.DateField()
    username_id = models.ForeignKey(User, on_delete=models.CASCADE)
