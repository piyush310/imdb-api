from rest_framework import serializers
from watchlist.models import WatchList
from watchlist.serializers.review import ReviewSerializer


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"
