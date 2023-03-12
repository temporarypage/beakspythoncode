import argparse
import requests
import time
import os
import webbrowser

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
    parser = argparse.ArgumentParser(description='Get YouTube channel information.')
    parser.add_argument('identifier', nargs='?', help='The YouTube username, channel ID, or handle (starting with @).')
    parser.add_argument('--key', required=False, help='Your Google API key.')
    args = parser.parse_args()

    if not args.identifier:
        args.identifier = input("Enter the YouTube username, channel ID, or handle (starting with @): ")

    api_key = args.key
    if not api_key:
        with open('api_key.txt', 'r') as f:
            api_key = f.read().strip()

    channel_id = get_channel_id(api_key, args.identifier)
    if not channel_id:
        print(f'Could not find channel ID for {args.identifier}')
        return

    file_name = f"{channel_id}.json"
    count = 1
    while os.path.exists(file_name):
        file_name = f"{channel_id}_{count}.json"
        count += 1

    channel_info = get_channel_info(api_key, channel_id)
    if not channel_info:
        print(f'Could not find information for channel {channel_id}')
        return

    with open(file_name, 'w') as f:
        f.write(str(channel_info))

    print(f'Channel information saved to {file_name}')
    webbrowser.open(file_name)


if __name__ == '__main__':
    main()
