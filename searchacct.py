import os
import urllib.request
import json
import datetime

# Check for api_key.txt file
if not os.path.isfile('api_key.txt'):
    print('api_key.txt file not found!')
    exit()

# Read API key from api_key.txt
with open('api_key.txt', 'r') as f:
    api_key = f.readline().strip()

# Ask for user input
year = input('What Year? ')
month = input('What Month? (Enter 1-12) ')
day = input('What Day? (Enter 1-31) ')
time = input('What Time? (Format: HH:MMAM/PM) ')
query = input('What Query? ')
subs = input('How many Subs? ')

# Create datetime object from user input
if year:
    dt = datetime.datetime(int(year), int(month), int(day))
    published_after = dt.isoformat() + 'Z'
    published_before = (dt + datetime.timedelta(days=1)).isoformat() + 'Z'

# Format time to ISO format
if time:
    time_obj = datetime.datetime.strptime(time, '%I:%M%p')
    iso_time = time_obj.strftime('%H:%M:%S') + 'Z'

url = 'https://www.googleapis.com/youtube/v3/search?part=snippet'
url += f'&key={api_key}'

if year:
    url += f'&publishedAfter={published_after}'
    url += f'&publishedBefore={published_before}'
if query:
    url += f'&q={query}'
if subs:
    url += f'&minSubscribers={subs}'
if time:
    url += f'&publishedAfter={published_after[0:11]}{iso_time}'
    url += f'&publishedBefore={published_before[0:11]}{iso_time}'

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

for item in data['items']:
    snippet = item['snippet']
    channel_id = snippet['channelId']
    channel_url = f'https://www.googleapis.com/youtube/v3/channels?id={channel_id}&part=snippet&key={api_key}'
    with urllib.request.urlopen(channel_url) as channel_data:
        channel_info = json.loads(channel_data.read().decode())
    channel_title = channel_info['items'][0]['snippet']['title']
    channel_year = channel_info['items'][0]['snippet']['publishedAt'][0:4]
    print(f'{channel_title} - {channel_year}')
