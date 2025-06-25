from django.db import models
from django.contrib.auth.models import User

class StudyGroup(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='study_groups',related_query_name='study_group')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

