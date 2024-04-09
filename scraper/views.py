from django.http import JsonResponse
from .models import YT_Video
from .models import store_latest_videos
from rest_framework import generics, filters
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination



def fetch_and_store_videos(request):
    api_key = ''
    search_query = ''
    store_latest_videos(api_key, search_query)
    return JsonResponse({'message': 'Videos fetched and stored successfully'})


class VideoListAPIView(generics.ListAPIView):
    queryset = YT_Video.objects.all().order_by('-published_at')
    serializer_class = VideoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['published_at']
    ordering = ['-published_at']
    pagination_class = LimitOffsetPagination  

class VideoSearchAPIView(generics.ListAPIView):
    queryset = YT_Video.objects.all().order_by('-published_at')
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


