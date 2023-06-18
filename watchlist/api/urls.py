from django.urls import path
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.watch_list import WatchListAV, WatchDetailAV
from watchlist.api.stream import StreamPlatformListAV, StreamPlatformDetailAV

urlpatterns = [
    path('api/v1/watch_list/', WatchListAV.as_view(), name='movie-list'),
    path('api/v1/watch_list/<int:id>',
         WatchDetailAV.as_view(), name='movie-detail'),
    path('api/v1/stream/',
         StreamPlatformListAV.as_view(),
         name='streaming-platform-list'),
    path('api/v1/stream/<int:id>',
         StreamPlatformDetailAV.as_view(),
         name='streaming-platform-detail'),
]
