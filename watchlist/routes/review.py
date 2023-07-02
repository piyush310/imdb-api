from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError
from watchlist.models import Review, WatchList
from watchlist.serializers import ReviewSerializer


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     return Review.objects.filter(pk=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreate(generics.CreateAPIView):

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)

        user = self.request.user

        review_query = Review.objects.filter(watchlist=watchlist,
                                             review_user=user)
        if review_query.exists():
            raise ValidationError("You have already reviewed this Movie")

        serializer.save(watchlist=watchlist, review_user=user)


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
#                    mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
