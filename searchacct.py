# hi nox
import os
import requests
import json
import webbrowser
import datetime

# check for api_key.txt file
if os.path.exists("api_key.txt"):
    with open("api_key.txt", "r") as f:
        api_key = f.read().strip()
else:
    print("api_key.txt not found")
    exit()

# set default values
year = "2005"
month = "06"
day = "01"

# ask for user input
published_after_input = input("Published After? (format: YYYY-MM-DD) default = {}-{}-{}: ".format(year, month, day)) or f"{year}-{month}-{day}"
published_before_days = input("How many days after Published After? default = 7: ") or "7"
published_before_input = (datetime.datetime.strptime(published_after_input, "%Y-%m-%d") + datetime.timedelta(days=int(published_before_days))).strftime("%Y-%m-%d")

# build url for youtube api request
url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&maxResults=50&key={api_key}&publishedAfter={published_after_input}T00:00:00Z&publishedBefore={published_before_input}T23:59:59Z"

# make request to youtube api
response = requests.get(url)

# parse response
channel_title_year = {}
response_json = response.json()
for item in response_json.get("items", []):
    channel_title = item["snippet"]["channelTitle"]
    channel_id = item["snippet"]["channelId"]
    if channel_title not in channel_title_year:
        channel_title_year[channel_title] = {"id": channel_id, "year": published_after_input[:4]}

# write to file
with open("channeltitle.txt", "w", encoding="utf-8") as f:
    for channel_title, info in channel_title_year.items():
        f.write(f"{channel_title} ({info['year']})\n")

# open saved file
with open(f"{year}.txt", "w", encoding="utf-8") as f:
    for channel_title, info in channel_title_year.items():
        channel_id = info["id"]
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&type=video&maxResults=50&key={api_key}"
        response = requests.get(url)
        response_json = response.json()
        for item in response_json.get("items", []):
            title = item["snippet"]["title"]
            f.write(f"{title}\n")

# open saved file
webbrowser.open("channeltitle.txt")
