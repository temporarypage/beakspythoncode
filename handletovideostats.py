import os
import requests
import json

# get directory of this Python file
dir_path = os.path.dirname(os.path.realpath(__file__))

# check for api_key.txt
if not os.path.exists(os.path.join(dir_path, "api_key.txt")):
    print("Error: api_key.txt not found.")
    exit()

# read API key from api_key.txt
with open(os.path.join(dir_path, "api_key.txt")) as f:
    api_key = f.read().strip()

# function to get channel ID from handle
def get_channel_id(api_key, identifier):
    if identifier.startswith('@'):
        url = f"https://yt.jaybee.digital/api/channels?part=channels&handle={identifier[1:]}"
        retries = 0
        while True:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    channel_id = response.json()["items"][0]["id"]
                    if channel_id.startswith("UC"):
                        return channel_id
            except:
                retries += 1
                if retries > 3:
                    raise Exception("Failed to get channel ID")

n = int(input("Starting at newest, how many videos do you want statistics for? "))
handle_id = input("Enter Handle id: ")
channel_id = get_channel_id(api_key, handle_id)
if not channel_id:
    print(f"Error: Could not get channel ID for handle {handle_id}")
    exit()

url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50"
try:
    response = requests.get(url)
    data = json.loads(response.text)
    video_ids = [item['id']['videoId'] for item in data['items'] if item['id']['kind'] == 'youtube#video']
    video_data = []
    for i in range(n):
        url = f"https://www.googleapis.com/youtube/v3/videos?key={api_key}&id={video_ids[i]}&part=snippet,statistics"
        response = requests.get(url)
        data = json.loads(response.text)
        if 'tags' not in data['items'][0]['snippet']:
            print(f"No data found for video with id {video_ids[i]}")
            continue
        video_data.append({
            "title": data['items'][0]['snippet']['title'],
            "views": int(data['items'][0]['statistics']['viewCount']),
            "likes": int(data['items'][0]['statistics']['likeCount']),
            "dislikes": int(data['items'][0]['statistics']['dislikeCount']),
            "tags": data['items'][0]['snippet']['tags']
        })
    if not video_data:
        print("No data found for the given handle.")
except Exception as e:
    print(f"An error occurred: {e}")
