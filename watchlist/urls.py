from django.urls import include, path
from watchlist.routes import (WatchListAV, WatchDetailAV, StreamPlatformListAV,
                              StreamPlatformDetailAV, ReviewList, ReviewDetail,
                              ReviewCreate, StreamPlatform)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("stream", StreamPlatform, basename="streamplatform")

urlpatterns = [
    path('movies/', WatchListAV.as_view(), name='movie-list'),
    path('movie/<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('', include(router.urls)),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/',
         ReviewCreate.as_view(),
         name='review-create'),
]

#     path('stream/review/<int:pk>/',ReviewDetail.as_view(), name='review-detail'),
#     path('stream/', StreamPlatformListAV.as_view(),name='streamplatform-list'),
#     path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(),name='streamplatform-detail'),
#     path('review/', ReviewList.as_view(), name='review-list'),
