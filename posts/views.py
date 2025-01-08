from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from posts.models import Post
from posts.serializers import PostModelSerializer


@method_decorator(csrf_exempt, name='dispatch')
class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


@method_decorator(csrf_exempt, name='dispatch')
class PostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
