import os

if os.path.exists("config.txt"):
    discord_username = ""
    api_key = ""
    avatar_url = ""
    with open("config.txt", "r") as f:
        for line in f:
            if "discord_username" in line:
                discord_username = line.split("=")[1].strip().strip('"')
            elif "api_key" in line:
                api_key = line.split("=")[1].strip().strip('"')
            elif "avatar_url" in line:
                avatar_url = line.split("=")[1].strip().strip('"')
    if not discord_username:
        discord_username = "Anonymous"
    if not api_key:
        api_key = ""
    if not avatar_url:
        avatar_url = "https://i.imgur.com/URC6SKP.png"
else:
    create_config = input("config.txt file not found! Do you want to create one? (Y/N): ")
    if create_config.upper() == "Y":
        discord_username = input("Enter your discord username for suggestions: ")
        api_key = input("enter your api_key for googleapis.com: ")
        avatar_url = input("Enter your Discord webhook profile picture URL: ")
        lines = []
        if os.path.exists("config.txt"):
            with open("config.txt", "r") as f:
                for line in f:
                    if "discord_username" in line:
                        line = f"discord_username = \"{discord_username}\"\n"
                    elif "api_key" in line:
                        line = f"api_key = \"{api_key}\"\n"
                    elif "avatar_url" in line:
                        line = f"avatar_url = \"{avatar_url}\"\n"
                    lines.append(line)
        else:
            lines.append(f"discord_username = \"{discord_username}\"\n")
            lines.append(f"api_key = \"{api_key}\"\n")
            lines.append(f"avatar_url = \"{avatar_url}\"\n")
        with open("config.txt", "w") as f:
            f.writelines(lines)
    else:
        discord_username = "Anonymous"
        api_key = ""
        avatar_url = "https://i.imgur.com/URC6SKP.png"
