import json
import subprocess

with open("Settings.json", "r") as file:
    config = json.load(file)

if config["launchsetting"] == 1:
    print("1")
    subprocess.Popen(["python", "KLLWindow.pyw"])
else:
    print("0")

