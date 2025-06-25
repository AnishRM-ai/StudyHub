from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    subjects = models.JSONField(default=list)
    strengths = models.JSONField(default=list)
    availability = models.JSONField(default=dict)
    timezone = models.CharField(max_length=50, default="UTC")

    def __str__(self):
        return self.user.username
