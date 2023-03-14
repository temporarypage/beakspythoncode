import os

if not os.path.exists("config.txt"):
    print("config.txt file not found! Creating one...")
    discord_username = input("Enter your discord username for suggestions: ")
    api_key = input("Before we get started, enter your api_key for googleapis.com: ")
    with open("config.txt", "w") as f:
        f.write(f"discord_username = \"{discord_username}\"\n")
        f.write(f"api_key = \"{api_key}\"\n")
else:
    discord_username = ""
    api_key = ""
    with open("config.txt", "r") as f:
        for line in f:
            if "discord_username" in line:
                discord_username = line.split("=")[1].strip().strip('"')
            elif "api_key" in line:
                api_key = line.split("=")[1].strip().strip('"')

    if not discord_username:
        discord_username = input("Enter your discord username for suggestions: ")
        with open("config.txt", "a") as f:
            f.write(f"discord_username = \"{discord_username}\"\n")
    if not api_key:
        api_key = input("Before we get started, enter your api_key for googleapis.com: ")
        with open("config.txt", "a") as f:
            f.write(f"api_key = \"{api_key}\"\n")

# we can use discord_username and api_key accordingly
