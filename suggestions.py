# suggestions
import requests
import datetime
beak = "https://discord.com/api/webhooks/1084522191485403"
myrealname = beak + "267/PZI--rnJKwVyMWxR"
WEBHOOK_URL = myrealname + "LkAkGGQbgkdqInnDh81p99XZr0TvSnYd6Cco5I3O30ZmxN99TpEO"

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
