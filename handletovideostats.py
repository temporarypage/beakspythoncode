# This gets tag info, like info, etc from a handles newest video(s)
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

# prompt user for input
print("Starting at newest, how many videos do you want statistics for?")
number_of_videos = input()

print("Enter Handle id:")
handle_id = input()

# get channel ID based on handle ID
url = f"https://yt.jaybee.digital/api/channels?part=channels&handle={handle_id[1:]}"
retries = 0
while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            channel_id = response.json()["items"][0]["id"]
            if channel_id.startswith("UC"):
                break
    except:
        pass
    retries += 1
    if retries >= 5:
        print("Error: failed to retrieve channel ID.")
        exit()

# fetch statistics and tags for channel's newest videos
url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults={number_of_videos}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for item in data["items"]:
        if item["id"]["kind"] == "youtube#video":
            video_id = item["id"]["videoId"]
            # fetch statistics
            url = f"https://www.googleapis.com/youtube/v3/videos?key={api_key}&id={video_id}&part=statistics"
            response = requests.get(url)
            if response.status_code == 200:
                statistics = response.json()["items"][0]["statistics"]
            else:
                statistics = {}

            # fetch tags
            url = f"https://www.googleapis.com/youtube/v3/videos?key={api_key}&id={video_id}&part=snippet"
            response = requests.get(url)
            if response.status_code == 200:
                tags = response.json()["items"][0]["snippet"]["tags"]
            else:
                tags = []

            # save data to file
            data = {
                "statistics": statistics,
                "tags": tags
            }
            with open(os.path.join(dir_path, f"{video_id}.json"), "w") as f:
                json.dump(data, f, indent=4)
            # open the file in default text editor
            os.startfile(os.path.join(dir_path, f"{video_id}.json"))

print("Video(s) have been saved to project folder. Enter any key to exit.")
input()
