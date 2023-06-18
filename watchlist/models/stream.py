
from django.db import models

class StreamPlaform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

