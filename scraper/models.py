from django.db import models
from .tools import fetch_latest_videos

# Create your models here.
class YT_Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()
        
    def __str__(self):
        return self.title

def store_latest_videos(api_keys, search_query):
    lastVideoTime = YT_Video.objects.order_by('-published_at').first().published_at
    print(lastVideoTime)
    formatted_time= lastVideoTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    videos = fetch_latest_videos(api_keys, search_query, last_video_time=formatted_time)
    for video in videos:
        YT_Video.objects.create(
            title=video['snippet']['title'],
            description=video['snippet']['description'],
            published_at=video['snippet']['publishedAt'],
            thumbnail_url=video['snippet']['thumbnails']['default']['url']
        )