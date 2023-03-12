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
month = input('What Month? ').capitalize()
if not month:
    month = 'January'
day = input('What Day? (if left blank it will automatically set to minimum dates for all) ') or '01'
time = input('What Time? (e.g 12:00AM) ') or '12:00AM'
query = input('What Query? (can be left blank) ')
subs = input('How many Subs? (can be left blank)')

try:
    datetime.strptime(f'{year}-{month}-{day} {time}', '%Y-%B-%d %I:%M%p')
except ValueError:
    print('Invalid date/time format!')
    exit()

url = 'https://www.googleapis.com/youtube/v3/search?part=snippet'
url += f'&key={api_key}'

if year:
    url += f'&publishedAfter={year}-{month}-{day}T{time}Z'
    url += f'&publishedBefore={year}-{month}-{day}T{time}Z'
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
