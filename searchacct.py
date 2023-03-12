import os
import urllib.request
import json

# Check for api_key.txt file
if not os.path.isfile('api_key.txt'):
    print('api_key.txt file not found!')
    exit()

# Read API key from api_key.txt
with open('api_key.txt', 'r') as f:
    api_key = f.readline().strip()

# Ask for user input
year = input('What Year? ')
month = input('What Month? ')
day = input('What Day? ')
time = input('What Time? ')
query = input('What Query? ')
subs = input('How many Subs? ')

url = 'https://www.googleapis.com/youtube/v3/search?part=snippet'
url += f'&key={api_key}'

if year:
    if month:
        if day:
            if time:
                date_time = f'{year}-{month}-{day}T{time}:00Z'
                url += f'&publishedAfter={date_time}'
                url += f'&publishedBefore={date_time}'
            else:
                date = f'{year}-{month}-{day}'
                url += f'&publishedAfter={date}T00:00:00Z'
                url += f'&publishedBefore={date}T23:59:59Z'
        else:
            url += f'&publishedAfter={year}-{month}-01T00:00:00Z'
            url += f'&publishedBefore={year}-{month}-31T23:59:59Z'
    else:
        url += f'&publishedAfter={year}-01-01T00:00:00Z'
        url += f'&publishedBefore={year}-12-31T23:59:59Z'
if query:
    url += f'&q={query}'
if subs:
    url += f'&minSubscribers={subs}'

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
