from django.db import models
from watchlist.models import WatchList
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(5)])
    description = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList,
                                  on_delete=models.CASCADE,
                                  related_name="reviews")

    def __str__(self):
        return str(self.rating) + "-" + self.watchlist.title
