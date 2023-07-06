from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform
from watchlist.serializers.review import ReviewSerializer


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"

    def create(self, validated_data):
        platform_name = validated_data.pop('platform')["name"]
        platform = StreamPlatform.objects.get(id=platform_name)
        validated_data['platform'] = platform
        return super().create(validated_data)
