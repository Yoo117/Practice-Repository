from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignupView, ProfileView, EditProfileView, ChangePasswordView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('password/change/', ChangePasswordView.as_view(), name='change_password'),
]