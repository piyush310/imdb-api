# from rest_framework import serializers
# from watchlist.models.stream import StreamPlaform
# from watchlist.models.watchlist import WatchList

# hyperlink serializer
# class StreamPlatformSerializer(serializers.ModelSerializer):
#     # watchlist = WatchListSerializer(many=True, read_only = True)

#     # return only __str__
#     # watchlist = serializers.StringRelatedField(many=True, read_only=True)

#     watchlist = serializers.HyperlinkedRelatedField(
#         many=True, read_only=True, view_name="movie-detail",
#         lookup_field="id")
#     class Meta:
#         model = StreamPlaform
#         fields = "__all__"

#ModelSerlializer
# class MovieSerializer(serializers.ModelSerializer):

#     name_length = serializers.SerializerMethodField()

#     # custom method
#     def get_name_length(self, object):
#         return len(object.name)

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError(
#                 "Name must be at least 2 characters long")
#         return value

#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError(
#                 "Name and description should not be the same")
#         return data

#     class Meta:
#         model = Movie
#         fields = "__all__"
# fields = ["id", "name", "description"]
# exclude = ["name"]

# Serializers
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError(
#             "Name must be at least 2 characters long")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     # def validate_name(self, value):
#     #     if len(value)<2:
#     #         raise serializers.ValidationError("Name must be at least 2 characters long")
#     #     return value

#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError(
#                 "Name and description should not be the same")
#         return data

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description',
#                                                   instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
