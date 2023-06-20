from django.urls import path
from watchlist.routes import WatchListAV, WatchDetailAV, StreamPlatformListAV, StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path('watch_list/', WatchListAV.as_view(), name='movie-list'),
    path('watch_list/<int:id>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(),
         name='streamplatform-list'),
    path('stream/<int:id>/',
         StreamPlatformDetailAV.as_view(),
         name='streamplatform-detail'),
    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
