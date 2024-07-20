from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, FileUploadView

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]
