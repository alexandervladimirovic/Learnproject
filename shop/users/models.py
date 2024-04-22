from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='_profile_images')
    contact_number = models.CharField(max_length=50, default='+79123456789')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


    def __str__(self):
        return self.user.username