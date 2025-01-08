from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'user__username', 'created_datetime'
    ordering = 'title',
    list_filter = 'title', 'user__username'
    search_fields = 'title', 'user__username'
    list_display_links = 'title',
