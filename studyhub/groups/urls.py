from rest_framework.routers import DefaultRouter
from .views import StudyGroupViewSet

router = DefaultRouter()
router.register('', StudyGroupViewSet)

urlpatterns = router.urls
