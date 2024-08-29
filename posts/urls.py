from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list,),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('tag/<slug:tag_slug>/', views.tag_posts, name='tag_posts'),
    path('search/', views.search_posts, name='search_posts'),
]