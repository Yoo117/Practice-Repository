from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, User
from django.db import models

class CustomUserManager(UserManager):
    # 일반 유저 생성
    def create_user(self, nickname, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        if not nickname:
            raise ValueError('닉네임은 필수입니다.')

        email = self.normalize_email(email)
        user = self.model(
            nickname=nickname,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # 관리자 생성
    def create_superuser(self, nickname, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser는 is_staff=True이어야 합니다.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser는 is_superuser=True이어야 합니다.')

        return self.create_user(nickname, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default_profile_picture.png')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager() # 해당 클래스를 매니저로 설정

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.nickname

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_notifications')
    message = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)  # 알림 클릭 시 이동할 URL
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.nickname} - {self.message}"

    class Meta:
        ordering = ['-created_at']  # 최신 알림이 먼저 표시되도록 정렬
