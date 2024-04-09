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

def store_latest_videos(api_key, search_query):
    videos = fetch_latest_videos(api_key, search_query)
    for video in videos:
        YT_Video.objects.create(
            title=video['snippet']['title'],
            description=video['snippet']['description'],
            published_at=video['snippet']['publishedAt'],
            thumbnail_url=video['snippet']['thumbnails']['default']['url']
        )