from googleapiclient.discovery import build

def fetch_latest_videos(api_key, search_query, max_results=10):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part='snippet',
        q=search_query,
        type='video',
        order='date',
        maxResults=max_results
    )
    response = request.execute()
    return response.get('items', [])