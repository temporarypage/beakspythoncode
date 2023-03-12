import urllib.request
from datetime import datetime
import pytz
import json
import requests

print("Getting 10 trending video titles")

    # fetch top 10 trending videos and their titles
    url = f"https://www.googleapis.com/youtube/v3/videos?key={api_key}&chart=mostPopular&part=snippet&maxResults=10"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        titles = [item["snippet"]["title"] for item in data["items"]]
    
        # save data to file
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(os.path.join(dir_path, f"trending{timestamp}.json"), "w") as f:
            json.dump(titles, f, indent=4)

        print(f"Video titles have been saved to trending{timestamp}.json. Enter any key to exit.")
        input()
    else:
        titles = []
        print("Error occurred while fetching trending videos.")
