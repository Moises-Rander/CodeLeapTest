from rest_framework import serializers
from posts.models import Post
from users.serializers import UserSerializer

class PostModelSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'user', 'created_datetime', 'title', 'content']
