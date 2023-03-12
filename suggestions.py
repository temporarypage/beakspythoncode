# suggestions
import requests
import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1084366056916783124/KqPsGovEbWhVRb9OfGE3lS9iIki0d-IkR0BRclI9WTcgONKMu_G1UsEIhFQ8I7X3UjSE"

# prompt user for suggestion
suggestion = input("Suggestions? ")

# get current timestamp
timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# create payload
payload = {
    "content": f"[{timestamp}] {suggestion}"
}

# post payload
response = requests.post(WEBHOOK_URL, json=payload)

# check if request was successful
if response.status_code == 204:
    print("Thanks for the suggestion, it will be reviewed and might be added!")
else:
    print("Error posting suggestion.")
