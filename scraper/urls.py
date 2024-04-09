from django.urls import path
from .views import VideoListAPIView, VideoSearchAPIView

urlpatterns = [
    path('videos/', VideoListAPIView.as_view(), name='video_list'),
    path('videos/search/', VideoSearchAPIView.as_view(), name='video_search'),
]
