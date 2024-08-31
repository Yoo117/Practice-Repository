from django.urls import path
from .views import (
    SignupView,
    CustomLoginView, 
    CustomLogoutView, 
    ProfileView,
    EditProfileView,
    ChangePasswordView
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('password/change/', ChangePasswordView.as_view(), name='change_password'),
]
