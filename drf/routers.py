from rest_framework.routers import DefaultRouter

from dropbox.viewsets import SecureViewSet

router = DefaultRouter()
router.register('dropbox', SecureViewSet, basename='dropbox')
urlpatterns = router.urls