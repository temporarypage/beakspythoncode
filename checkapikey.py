# Checks for api key in project folder
import importlib
import subprocess
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
api_key_file = os.path.join(dir_path, "api_key.txt")

if not os.path.exists(api_key_file):
    print("api_key.txt not found. Please create this file in the project folder and put your YouTube Data API key in it.")
    input("Press any key to exit.")
    exit()

# read api key from file
with open(api_key_file) as f:
    api_key = f.read().strip()

def install_module(module_name):
    subprocess.check_call(["pip", "install", module_name])

# Check if necessary modules are installed
modules_needed = ['requests', 'pytz', 'urllib.request', 'datetime', 'json']
for module_name in modules_needed:
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"{module_name} module not found")
        install = input(f"Do you want to install {module_name} module? (Y/N) ").lower()
        if install == 'y':
            install_module(module_name)
        else:
            print(f"{module_name} module not found, exiting...")
            exit()
