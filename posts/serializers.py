from rest_framework import serializers
from posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
