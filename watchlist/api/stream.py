
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist.models.stream import StreamPlaform
from watchlist.api.serializers import StreamPlatformSerializer


class StreamPlatformListAV(APIView):
    def get(self, request):
        movies = StreamPlaform.objects.all()
        serializer = StreamPlatformSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
    def get(self, request, id):
        try:
            movie = StreamPlaform.objects.get(id=id)
            serializer = StreamPlatformSerializer(movie)
            return Response(serializer.data)
        except StreamPlaform.DoesNotExist:
            return Response({"error": "Streaming Plaform not found"},
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        movie = StreamPlaform.objects.get(id=id)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = StreamPlaform.objects.get(id=id)
        movie.delete()
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_204_NO_CONTENT)

