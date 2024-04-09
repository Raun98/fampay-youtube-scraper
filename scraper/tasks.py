from celery import shared_task
from .models import store_latest_videos

@shared_task
def fetch_and_store_celery(api_keys,search_query):
    store_latest_videos(api_keys=api_keys, search_query=search_query)