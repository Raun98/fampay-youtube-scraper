from rest_framework import serializers
from .models import YT_Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YT_Video
        fields = ['id', 'title', 'description', 'published_at', 'thumbnail_url']
