from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="User account",
        on_delete=models.CASCADE,
        related_name="profile"
    )
    tel = models.CharField(
        verbose_name="Tel number",
        max_length=24
    )