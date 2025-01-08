from django.urls import path
from posts.views import PostCreateListView, PostDetailUpdateDeleteView


urlpatterns = [
    path('posts/', PostCreateListView.as_view(), name='post-create-list'),
    path('posts/<int:pk>/', PostDetailUpdateDeleteView.as_view(), name='post-detail-update-delete'),
]
