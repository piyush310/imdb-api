from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer


class MovieListAV(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MovieDetailAV(APIView):
    def get(self, request, id):
        try:
            movie = Movie.objects.get(id=id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"},
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = Movie.objects.get(id=id)
        movie.delete()
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail(request, id):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(id=id)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
#         except Movie.DoesNotExist:
#             return Response({"error": "Movie not found"},
#                             status=status.HTTP_404_NOT_FOUND)

#     if request.method == "PUT":
#         movie = Movie.objects.get(id=id)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "DELETE":
#         movie = Movie.objects.get(id=id)
#         movie.delete()
#         content = {'please move along': 'nothing to see here'}
#         return Response(content, status=status.HTTP_204_NO_CONTENT)
