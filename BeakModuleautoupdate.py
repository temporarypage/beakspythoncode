import urllib.request

site = "https://raw.githubusercontent.com/temporarypage/beakspythoncode/main/"


exec(urllib.request.urlopen(site + "ShortBeakModule.py").read())
