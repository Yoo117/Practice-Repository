from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.conf import settings

class CustomUserManager(UserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser는 is_staff=True이어야 합니다.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser는 is_superuser=True이어야 합니다.')
        
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default_profile_picture.png')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nickname']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f'{self.username} ({self.nickname})'
    
    def get_short_name(self):
        return self.nickname

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
