import json
import subprocess
import time

time.sleep(1)
with open("Settings.json", "r") as file:
    config = json.load(file)

if config["SafeMode"] == 0:
    print("Safe Mode Deactivated")
    subprocess.Popen(["python", "KLLWindow.py"])
    time.sleep(9)
else:
    print("Safe Mode Activated")
    time.sleep(9)
