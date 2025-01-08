from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'username__username', 'created_datetime'
    ordering = 'title',
    list_filter = 'title', 'username__username'
    search_fields = 'title', 'username__username'
    list_display_links = 'title',
