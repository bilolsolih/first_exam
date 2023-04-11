from django.db import models
from apps.common.models import BaseModel


class Profile(BaseModel):
    profile_photo = models.ImageField(upload_to='images/profiles/%Y/%m/%d/', null=True, blank=True)
    user = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"Profile for {self.user.username}"
