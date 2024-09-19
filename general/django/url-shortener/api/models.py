from django.db import models


class Url(models.Model):
    original_url = models.CharField(max_length=100)
