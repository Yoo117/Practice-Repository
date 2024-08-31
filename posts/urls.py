from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CategoryPostsView,
    TagPostsView,
    SearchPostsView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('category/<slug:slug>/', CategoryPostsView.as_view(), name='category_posts'),
    path('tag/<slug:slug>/', TagPostsView.as_view(), name='tag_posts'),
    path('search/', SearchPostsView.as_view(), name='search_posts'),
]