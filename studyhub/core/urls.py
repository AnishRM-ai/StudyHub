from django.urls import path
from .views import ProfileView, ProfileCreateOrUpdateView

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile-detail'),
    path('', ProfileCreateOrUpdateView.as_view(), name='my-profile'),
]
