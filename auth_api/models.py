from django.db import models
import secrets
import string
from django.utils import timezone
from datetime import timedelta

class User(models.Model):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    @classmethod
    def create_otp(cls, user):
        # Generate a 6-digit numeric OTP
        code = ''.join(secrets.choice(string.digits) for _ in range(6))
        expires_at = timezone.now() + timedelta(minutes=5)  # OTP valid for 5 minutes
        return cls.objects.create(user=user, code=code, expires_at=expires_at)

    def is_valid(self):
        return timezone.now() <= self.expires_at

    def __str__(self):
        return f"OTP for {self.user.email}"