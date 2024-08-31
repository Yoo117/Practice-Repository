from django.urls import path

from .views import (
    AddCommentView,
    AddReplyView,
    EditCommentView,
    DeleteCommentView,
    LikePostView,
    BookmarkPostView,
    NotificationsView
)

urlpatterns = [
    path('post/<int:post_id>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:comment_id>/reply/', AddReplyView.as_view(), name='add_reply'),
    path('comment/<int:comment_id>/edit/', EditCommentView.as_view(), name='edit_comment'),
    path('comment/<int:comment_id>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
    path('post/<int:post_id>/like/', LikePostView.as_view(), name='like_post'),
    path('post/<int:post_id>/bookmark/', BookmarkPostView.as_view(), name='bookmark_post'),
    path('notifications/', NotificationsView.as_view(), name='notifications'),
]