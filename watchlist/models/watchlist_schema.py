from django.db import models
from watchlist.models.stream_schema import StreamPlatform


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    platform = models.ForeignKey(StreamPlatform,
                                 on_delete=models.CASCADE,
                                 related_name="watchlist")

    def __str__(self):
        return self.title
