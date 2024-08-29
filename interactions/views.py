from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, Comment, Like, Bookmark, Notification
from .forms import CommentForm, ReplyForm, BookmarkForm, NotificationForm

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'interactions/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})

class AddReplyView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = ReplyForm
    template_name = 'interactions/add_reply.html'

    def form_valid(self, form):
        parent_comment = get_object_or_404(Comment, pk=self.kwargs['comment_id'])
        form.instance.author = self.request.user
        form.instance.post = parent_comment.post
        form.instance.parent = parent_comment
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

class EditCommentView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'interactions/edit_comment.html'
    pk_url_kwarg = 'comment_id'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'interactions/delete_comment.html'
    pk_url_kwarg = 'comment_id'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

class LikePostView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            # 유저가 이미 좋아요를 눌렀을 시, 그 좋아요를 제거합니다.
            like.delete()
            liked = False
        else:
            liked = True

        return JsonResponse({'liked': liked, 'likes_count': post.like_set.count()})

class BookmarkPostView(LoginRequiredMixin, CreateView):
    model = Bookmark
    form_class = BookmarkForm
    http_method_names = ['post']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def form_invalid(self, form):
        # 북마크가 이미 존재 시, 제거합니다.
        Bookmark.objects.filter(user=self.request.user, post_id=self.kwargs['post_id']).delete()
        return JsonResponse({'bookmarked': False})

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})

class NotificationsView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'interactions/notifications_list.html'
    context_object_name = 'notifications'
    form_class = NotificationForm

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            notification_id = form.cleaned_data['notification_id']
            try:
                notification = Notification.objects.get(id=notification_id, recipient=request.user)
                notification.is_read = True
                notification.save()
                return JsonResponse({'status': 'success'})
            except Notification.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Notification does not exist'}, status=404)
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)