from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from watchlist.permissions.permissions import IsAdminOrReadOnly
from watchlist.models import StreamPlatform as StreamPlatforms
from watchlist.serializers import StreamPlatformSerializer
from django.shortcuts import get_object_or_404


class StreamPlatform(viewsets.ModelViewSet):
    queryset = StreamPlatforms.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAdminOrReadOnly]


"""
Other method to create view
class StreamPlatformListAV(generics.ListAPIView):
    queryset = StreamPlatforms.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAdminOrReadOnly]

class StreamPlatformDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatforms.objects.all
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAdminOrReadOnly]
"""
"""
Other method to create view
class StreamPlatform(viewsets.ViewSet):
def list(self, request):
    queryset = StreamPlatforms.objects.all()
    serializer = StreamPlatformSerializer(queryset, many=True)
    return Response(serializer.data)

def retrieve(self, request, pk=None):
    queryset = StreamPlatforms.objects.all()
    watchlist = get_object_or_404(queryset, pk=pk)
    serializer = StreamPlatformSerializer(watchlist)
    return Response(serializer.data)

def create(self, request):
    serializer = StreamPlatformSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

class StreamPlatformListAV(APIView):
    def get(self, request):
        movies = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(movies,
                                              many=True,
                                              context={'request': request})
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
            movie = StreamPlatform.objects.get(id=id)
            serializer = StreamPlatformSerializer(movie,
                                                  context={'request': request})
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "Streaming Plaform not found"},
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        movie = StreamPlatform.objects.get(id=id)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = StreamPlatform.objects.get(id=id)
        movie.delete()
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_204_NO_CONTENT)
"""
