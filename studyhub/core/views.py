from django.shortcuts import render

from rest_framework import generics, permissions
from .models import UserProfile
from .serializers import UserProfileSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class ProfileCreateOrUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Ensure each user has only one profile
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile
