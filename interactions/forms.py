from django import forms

from .models import Comment, Bookmark, Notification

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = []  # URL의 post_id를 사용하므로 필드가 필요하지 않습니다.

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['is_read']