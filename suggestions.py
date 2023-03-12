import requests
half = "https://discord.com/api/webhooks/1084528717717581824/nibnXAuN460cD-f"
suggestion = input("Enter your suggestion: ")
timestamp = datetime.now(pytz.timezone('US/Eastern')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
message = {
    "content": f"New suggestion: {suggestion}\nTimestamp: {timestamp}",
    "username": "Suggestion Bot",
    "avatar_url": "https://i.imgur.com/4M34hi2.png"
}
headers = {
    "Content-Type": "application/json"
}
webhook_url = half + "bxC2eJSP__FquEpIBdwcg8KyKqNyXUIgnSXVk6cLbZacm6lGz1Rqv"
request = urllib.request.Request(webhook_url, json.dumps(message).encode(), headers=headers)
response = urllib.request.urlopen(request)
print("Your suggestion will be reviewed and maybe be added to the list!")
send_suggestion()
