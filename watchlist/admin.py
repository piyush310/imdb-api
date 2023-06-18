from django.contrib import admin
from watchlist.models import StreamPlatform, WatchList, Review

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
