from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField()
    image = models.ImageField(upload_to="avatars", null=False, default="no_image.jpg")

    def __str__(self):
        return self.user.username