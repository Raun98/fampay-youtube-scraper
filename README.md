# Youtube Scraper

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Setup Guide:

- Start by cloning this project to your computer.
- Install dependencies using `pip install -r requirements.txt` in your terminal.
- As the project runs on YouTube's Data v3 API, an API key is required. It can be obtained by [clicking here](https://developers.google.com/youtube/v3/getting-started)
- Navigate to the services.py file, find the settings variable **YOUTUBE_API_KEY = [ ... ]**, and adding your __API_KEY__ to this list.
- Open three terminals __parallelly__, on all of them change directory to the YoutubeSearchProject directory. There should be a _manage.py_ file in this folder.
- On one terminal window, run `celery -A server beat -l INFO`
- On the second, run `celery -A server worker -l info`
- On the other terminal window, run `python3 manage.py runserver`

# Docker Setup:
- Clone the repo and run `docker-compose build`
- Once done building, run `docker-compose up -d`
- And to check logs you can run `docker-compose logs -f`

Django returns a URL to your local host, follow that to find the dashboard.

Thank you for reading!
