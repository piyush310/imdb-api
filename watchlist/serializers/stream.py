from rest_framework import serializers
from watchlist.models import StreamPlatform
from watchlist.serializers.watchlist import WatchListSerializer


class StreamPlatformSerializer(serializers.ModelSerializer):

    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
