from django.urls import include, path
from rest_framework.routers import DefaultRouter
from watchlist.routes import (WatchListAV, WatchDetailAV, WatchListCreateAV,
                              ReviewList, ReviewDetail, ReviewCreate,
                              StreamPlatform)

router = DefaultRouter()
router.register("stream", StreamPlatform, basename="streamplatform")

# Movies Routes
urlpatterns = [
    path('movies/', WatchListAV.as_view(), name='movie-list'),
    path('movie/', WatchListCreateAV.as_view(), name='movie-list'),
    path('movie/<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
]

# Reviews Routes
urlpatterns += [
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('movie/<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('movie/<int:pk>/review-create/',
         ReviewCreate.as_view(),
         name='review-create'),
]

# Streams Routes
urlpatterns += [
    path('', include(router.urls), name='stream'),
]
