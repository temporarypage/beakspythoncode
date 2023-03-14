import urllib.request
import colorama
from colorama import Fore, Style

colorama.init()

site = "https://raw.githubusercontent.com/temporarypage/beakspythoncode/main/"


exec(urllib.request.urlopen(site + "checkapikey.py").read())
exec(urllib.request.urlopen(site + "ver.py").read())
exec(urllib.request.urlopen(site + "BEAKMODULE/beakmoduleprinting.py").read())

options = [
    "Get Channel Data From Handle, userid, etc...",
    "Handle To Newest Video Statistics",
    "Get Trending Videos",
    "Add Suggestions For A Number (Fixed!)",
    "Search Accts For Claiming Purposes Based Off Of Terms",
    "Configuration (New!) Credit Euphoria",
    "Search Accts Based off Subs (New!)"
]

while True:
    for i, option in enumerate(options):
        print(Fore.RED + f"[{i+1}] {option}" + Style.RESET_ALL)
        
    choice = input("Enter a number: ")
    
    if choice == "1":
        exec(urllib.request.urlopen(site + "banneryt.py").read())            
    elif choice == "2":
        exec(urllib.request.urlopen(site + "handletovideostats.py").read())
    elif choice == "3":
        exec(urllib.request.urlopen(site + "trendingvideos.py").read())
    elif choice == "4":
        exec(urllib.request.urlopen(site + "suggestions.py").read())                  
    elif choice == "5":
        exec(urllib.request.urlopen(site + "handletosubs.py").read())        
    elif choice == "6":
        exec(urllib.request.urlopen(site + "config.py").read())        
    elif choice == "7":
        exec(urllib.request.urlopen(site + "subterms.py").read()) 
        break
            
    else:
        print(Fore.MAGENTA + "Invalid option. Please choose a number between 1 and 8." + Style.RESET_ALL)
