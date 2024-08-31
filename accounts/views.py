from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView, UpdateView, TemplateView
from django.views.generic import ListView

from .models import User, Notification
from .forms import SignupForm, LoginForm, ProfileForm, ChangePasswordForm, NotificationForm

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logged_out.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user # 요청한 현재 사용자를 context에 추가
        return context

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('profile')

class NotificationsView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'accounts/notifications_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        # 현재 사용자가 받은 알림만을 필터링하여 반환
        return Notification.objects.filter(recipient=self.request.user)

    def post(self, request, *args, **kwargs):
        form = NotificationForm(request.POST)  # POST 요청을 기반으로 폼 생성
        if form.is_valid():
            notification_id = form.cleaned_data['notification_id']
            try:
                # 알림을 데이터베이스에서 조회
                notification = Notification.objects.get(id=notification_id, recipient=request.user)
                notification.is_read = True  # 알림을 읽음 상태로 변경
                notification.save()
                return JsonResponse({'status': 'success'})  # 성공 응답을 Json 형태로 반환
            except Notification.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Notification does not exist'}, status=404)
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)