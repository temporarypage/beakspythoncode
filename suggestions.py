import requests
import datetime
import pytz

real = "1824/nibnXAuN460cD-fbxC2eJSP__FquEpIBdwcg8KyKqNyXUIgnSXVk6cLbZacm6lGz1Rqv"
WEBHOOK_URL = "https://discord.com/api/webhooks/108452871771758" + real

# prompt user for suggestion
suggestion = input("Suggestions? ")

# get current timestamp
timestamp = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%m/%d/%Y %I:%M:%S%p EST")

# create payload
payload = {
    "username": "Suggestion Bot",
    "avatar_url": "https://i.imgur.com/4M34hi2.png",
    "content": f"Suggestion! Info:\nDate {timestamp}\n      suggestion: {suggestion}"
}

# post payload
response = requests.post(WEBHOOK_URL, json=payload)

# check if request was successful
if response.status_code == 204:
    print("Thanks for the suggestion, it will be reviewed and might be added!")
else:
    print("Error posting suggestion.")
