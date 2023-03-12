import os
import urllib.request
import json
from datetime import datetime

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
time = input('What Time? (e.g. 12:00AM) ')
query = input('What Query? ')
subs = input('How many Subs? ')
published_before = input('Published Before? ')
if published_before == '':
    published_before = '2005-01-01T00:00:00Z'
published_after = input('Published After? ')
if published_after == '':
    now = datetime.now()
    published_after = now.strftime('%Y-%m-%dT%H:%M:%SZ')

if month:
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if month.lower() in months:
        month = str(months.index(month.lower()) + 1)
    else:
        month = str(int(month))
if day:
    day = str(int(day))

url = 'https://www.googleapis.com/youtube/v3/search?part=snippet'
url += f'&key={api_key}'

if year:
    url += f'&publishedAfter={year}-{month or 1}-{day or 1}T{time or "00:00:00Z"}'
    url += f'&publishedBefore={year}-{month or 12}-{day or 31}T{time or "23:59:59Z"}'
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
