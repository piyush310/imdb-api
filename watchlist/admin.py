from django.contrib import admin
from watchlist.models.stream import StreamPlaform
from watchlist.models.watchlist import WatchList

admin.site.register(WatchList)
admin.site.register(StreamPlaform)
