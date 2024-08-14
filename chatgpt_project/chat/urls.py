from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatView.as_view(), name='chat'),
    path('chat/', views.ChatView.as_view(), name='chat'), 
]
