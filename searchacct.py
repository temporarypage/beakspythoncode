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

# Function to convert month name to number
def month_to_number(month_name):
    return datetime.datetime.strptime(month_name, "%B").month

# Ask for user input
year = input('What Year? ')
query = input('What Query? ')
subs = input('How many Subs? ')
published_before = input('Published Before? (e.g. Jan 1, 2022 12:00AM) ')
published_after = input('Published After? (e.g. Feb 1, 2022 12:00AM) ')

# Convert month name to number
if published_before:
    published_before = datetime.datetime.strptime(published_before, '%b %d, %Y %I:%M%p')
if published_after:
    published_after = datetime.datetime.strptime(published_after, '%b %d, %Y %I:%M%p')

url = 'https://www.googleapis.com/youtube/v3/search?part=snippet'
url += f'&key={api_key}'

if year:
    url += f'&publishedAfter={year}-01-01T00:00:00Z'
    url += f'&publishedBefore={year}-12-31T23:59:59Z'
if query:
    url += f'&q={query}'
if subs:
    url += f'&minSubscribers={subs}'
if published_before:
    url += f'&publishedBefore={published_before.isoformat()}Z'
if published_after:
    url += f'&publishedAfter={published_after.isoformat()}Z'

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
