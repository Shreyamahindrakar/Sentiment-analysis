from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DownloadCsv, ReviewViewSet, FileUploadView,GetFileIdWise

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('download_csv/',DownloadCsv.as_view(), name='download-csv'),
    path('get_file_id_wise/', GetFileIdWise.as_view(), name='get-file-id-wise'),
]
