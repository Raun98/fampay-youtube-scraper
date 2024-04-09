from django.http import JsonResponse
from .models import YT_Video
from .models import store_latest_videos
from rest_framework import generics, filters
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import render



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

def video_dashboard(request):
    videos = YT_Video.objects.all()
    title_contains = request.GET.get('title_contains')
    if title_contains:
        videos = videos.filter(title__icontains=title_contains)

    sort_by = request.GET.get('sort_by', '-published_at')
    videos = videos.order_by(sort_by)

    return render(request, 'scraper/dashboard.html', {'videos': videos})
