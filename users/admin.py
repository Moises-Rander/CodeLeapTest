from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'username',
    ordering = 'username',
    list_filter = 'username',
    search_fields = 'username',
    list_display_links = 'username',
