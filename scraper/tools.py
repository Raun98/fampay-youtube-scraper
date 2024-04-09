from googleapiclient.discovery import build
import time
# def fetch_latest_videos(api_key, search_query, max_results=10):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     request = youtube.search().list(
#         part='snippet',
#         q=search_query,
#         type='video',
#         order='date',
#         maxResults=max_results
#     )
#     response = request.execute()
#     return response.get('items', []) -- working code in case multiple api keys logic fails



def fetch_latest_videos(api_keys, search_query, last_video_time, max_results=10):
    for api_key in api_keys:
        try:
            youtube = build('youtube', 'v3', developerKey=api_key)
            request = youtube.search().list(
                part='snippet',
                q=search_query,
                type='video',
                order='date',
                maxResults=max_results,
                publishedAfter=last_video_time,
            )
            response = request.execute()
            return response.get('items', [])
        except Exception as e:
            if "quota" in str(e).lower():
                print(f"Quota exhausted for API key: {api_key}. Trying next key...")
                time.sleep(1)  
            else:
                raise
    print("All API keys exhausted. Failed to fetch latest videos.")
    return []