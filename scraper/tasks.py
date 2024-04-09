from celery import shared_task
from .models import store_latest_videos

@shared_task
def fetch_and_store_celery(api_key,search_query):
    store_latest_videos(api_key=api_key, search_query=search_query)