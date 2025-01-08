from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostCreateListView.as_view(), name='post-create-list'),
    path('posts/<int:pk>/', views.PostDetailUpdateDeleteView.as_view(), name='post-detail-update-delete'),
]
