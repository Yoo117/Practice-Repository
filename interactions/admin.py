from django.contrib import admin
from .models import Comment, Like, Bookmark, Notification

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at', 'updated_at', 'parent')
    list_filter = ('created_at', 'updated_at', 'post', 'author')
    search_fields = ('content', 'author__username', 'post__title')
    ordering = ('-created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at', 'user', 'post')
    search_fields = ('user__username', 'post__title')
    ordering = ('-created_at',)

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at', 'user', 'post')
    search_fields = ('user__username', 'post__title')
    ordering = ('-created_at',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'notification_type', 'actor', 'verb', 'target', 'created_at', 'is_read')
    list_filter = ('notification_type', 'is_read', 'created_at', 'recipient', 'actor')
    search_fields = ('actor__username', 'recipient__username', 'verb', 'target__title')
    ordering = ('-created_at',)
