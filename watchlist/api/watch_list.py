from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist.models.watchlist import WatchList
from watchlist.api.serializers import WatchListSerializer

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self, request, id):
        try:
            movie = WatchList.objects.get(id=id)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            return Response({"error": "Movie not found"},
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        movie = WatchList.objects.get(id=id)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = WatchList.objects.get(id=id)
        movie.delete()
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_204_NO_CONTENT)
