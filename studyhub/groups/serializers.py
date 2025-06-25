from rest_framework import serializers
from .models import StudyGroup
from django.contrib.auth.models import User

class StudyGroupSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = StudyGroup
        fields = ['id', 'name', 'subject', 'description', 'members', 'created_at']
