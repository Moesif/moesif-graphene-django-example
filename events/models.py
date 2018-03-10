from django.db import models
from django.conf import settings


# Defining Event model
class Event(models.Model):
    name = models.TextField(blank=True)
    url = models.URLField()