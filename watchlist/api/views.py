# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from watchlist.models import WatchList, StreamPlaform
# from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer


# class StreamPlatformListAV(APIView):
#     def get(self, request):
#         movies = StreamPlaform.objects.all()
#         serializer = StreamPlatformSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# class StreamPlatformDetailAV(APIView):
#     def get(self, request, id):
#         try:
#             movie = StreamPlaform.objects.get(id=id)
#             serializer = StreamPlatformSerializer(movie)
#             return Response(serializer.data)
#         except StreamPlaform.DoesNotExist:
#             return Response({"error": "Streaming Plaform not found"},
#                             status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, id):
#         movie = StreamPlaform.objects.get(id=id)
#         serializer = StreamPlatformSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         movie = StreamPlaform.objects.get(id=id)
#         movie.delete()
#         content = {'please move along': 'nothing to see here'}
#         return Response(content, status=status.HTTP_204_NO_CONTENT)


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
#     def get(self, request, id):
#         try:
#             movie = WatchList.objects.get(id=id)
#             serializer = WatchListSerializer(movie)
#             return Response(serializer.data)
#         except WatchList.DoesNotExist:
#             return Response({"error": "Movie not found"},
#                             status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, id):
#         movie = WatchList.objects.get(id=id)
#         serializer = WatchListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         movie = WatchList.objects.get(id=id)
#         movie.delete()
#         content = {'please move along': 'nothing to see here'}
#         return Response(content, status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = WatchListSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = WatchListSerializer(data=request.data)
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
#             serializer = WatchListSerializer(movie)
#             return Response(serializer.data)
#         except Movie.DoesNotExist:
#             return Response({"error": "Movie not found"},
#                             status=status.HTTP_404_NOT_FOUND)

#     if request.method == "PUT":
#         movie = Movie.objects.get(id=id)
#         serializer = WatchListSerializer(movie, data=request.data)
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
