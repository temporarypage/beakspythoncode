import urllib.request
from datetime import datetime
import pytz
import json
import requests
import colorama
from colorama import Fore, Style

colorama.init()

# site so i don't have to write the whole stinkin link
# Another note, im not trying to obfuscate to hide any malicious code, if you think it is malicious go to my github page "https://github.com/temporarypage/beakspythoncode/tree/main"
site = "https://raw.githubusercontent.com/temporarypage/beakspythoncode/main/"
# Checks for api_key.txt (made as link because it is clutter) note to self this didn't work on trendingpages maybe it wont work for others either
script_url = site + "checkapikey.py"
with urllib.request.urlopen(script_url) as url:
    exec(url.read())

script_url = site + "ver.py"
with urllib.request.urlopen(script_url) as url:
    exec(url.read())

print(Fore.MAGENTA + Style.BRIGHT + r'''
 ____  _____    _    _  __  __  __  ___  ____  _   _ _     _____ 
| __ )| ____|  / \  | |/ / |  \/  |/ _ \|  _ \| | | | |   | ____|
|  _ \|  _|   / _ \ | ' /  | |\/| | | | | | | | | | | |   |  _|  
| |_) | |___ / ___ \| . \  | |  | | |_| | |_| | |_| | |___| |___ 
|____/|_____/_/   \_\_|\_\ |_|  |_|\___/|____/ \___/|_____|_____|
''' + Style.RESET_ALL)
print(Fore.RED + "[1] Get Channel Data From Handle, userid, etc..." + Style.RESET_ALL)
print(Fore.RED + "[2] Handle To Newest Video Statistics" + Style.RESET_ALL)
print(Fore.RED + "[3] Get Trending Videos" + Style.RESET_ALL)
print(Fore.RED + "[4] Add Suggestions For A Number (Fixed!)" + Style.RESET_ALL)
print(Fore.RED + "[5] Search Accts For Claiming Purposes Based Off Of Terms" + Style.RESET_ALL)
print(Fore.RED + "[6] Exit BeakModule" + Style.RESET_ALL)


while True:
    choice = input("Enter a number: ")
    if choice == "1":
        # Making code smaller just so it is easier for me, you can check if it is malicious idrc
        script_url = site + "banneryt.py"
        with urllib.request.urlopen(script_url) as url:
            exec(url.read())
    elif choice == "2":
        # handle to newest video statistics, just enter handle and you can choose how many videos you want to get statistics of and yeah
        script_url = site + "handletovideostats.py"
        with urllib.request.urlopen(script_url) as url:
            exec(url.read())
    elif choice == "6":
        print("Exiting program...")
        break
    elif choice == "4":
        script_url = site + "suggestions.py"
        with urllib.request.urlopen(script_url) as url:
            exec(url.read())
    elif choice == "3":
        script_url = site + "trendingvideos.py"
        with urllib.request.urlopen(script_url) as url:
            exec(url.read())
    elif choice == "5":
        script_url = site + "searchacct.py"
        with urllib.request.urlopen(script_url) as url:
            exec(url.read())
    else:
        print(Fore.RED + "ooh you think you're so funny entering a number that isn't listed." + Style.RESET_ALL)
