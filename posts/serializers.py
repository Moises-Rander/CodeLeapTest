from rest_framework import serializers
from posts.models import Post
from users.models import User
from users.serializers import UserModelSerializer



class PostModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_get = UserModelSerializer(source='user', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'user_get', 'created_datetime', 'title', 'content']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = representation.pop('user_get')
        return representation
