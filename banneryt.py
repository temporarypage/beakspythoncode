import argparse
import requests
import time
import os
import webbrowser
import json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


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
                    break
            except:
                pass
            retries += 1
            if retries > 3:
                print(f"Response isn't loading because the handle is owned to an account that is bugged, probably @wathc")
                return None
            print(f"Response didn't load. Retrying in 5 seconds...")
            time.sleep(5)
    else:
        return identifier


def get_channel_info(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id
    )
    response = request.execute()
    if 'items' in response:
        return response['items'][0]
    return None


def main():
    # parse command-line arguments and get API key and channel ID...

    # create a unique file name for the channel information
    file_name = f"{channel_id}.json"
    count = 1
    while os.path.exists(file_name):
        file_name = f"{channel_id}_{count}.json"
        count += 1

    # get the channel information
    channel_info = get_channel_info(api_key, channel_id)
    if not channel_info:
        print(f'Could not find information for channel {channel_id}')
        return

    # write the channel information to a file
    with open(file_name, 'w') as f:
        json.dump(channel_info, f, indent=4)

    print(f'Channel information saved to {file_name}')
    webbrowser.open(file_name)


if __name__ == '__main__':
    main()
