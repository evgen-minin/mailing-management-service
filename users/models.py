from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    
    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='телефон', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='страна', blank=True, null=True)
    register_uuid = models.UUIDField(verbose_name='uuid', blank=True, null=True)
    is_manager = models.BooleanField(default=False)
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username