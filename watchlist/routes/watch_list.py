from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist.models import WatchList
from watchlist.serializers import WatchListSerializer
from rest_framework import generics


class WatchListAV(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


class WatchDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


# class WatchListAV(APIView):
#     def get(self, request):
#         movies = WatchList.objects.all()
#         serializer = WatchListSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class WatchDetailAV(APIView):
#     def get(self, request, pk):
#         try:
#             movie = WatchList.objects.get(pk=pk)
#             serializer = WatchListSerializer(movie)
#             return Response(serializer.data)
#         except WatchList.DoesNotExist:
#             return Response({"error": "Movie not found"},
#                             status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, pk):
#         movie = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         movie = WatchList.objects.get(pk=pk)
#         movie.delete()
#         content = {'please move along': 'nothing to see here'}
#         return Response(content, status=status.HTTP_204_NO_CONTENT)