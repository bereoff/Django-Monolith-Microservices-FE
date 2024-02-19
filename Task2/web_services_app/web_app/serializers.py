from rest_framework import serializers


class PostListSerializer(serializers.Serializer):
    _id = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()
    date_posted = serializers.DateTimeField()
