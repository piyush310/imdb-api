from django.urls import path
# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:id>', MovieDetailAV.as_view(), name='movie-detail'),
]
