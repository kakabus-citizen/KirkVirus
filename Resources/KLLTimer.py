import time
import subprocess
import json


with open("Settings.json", "r") as file:
    config = json.load(file)



if config["Crasher"] == 1:
    print("1")
    time.sleep(25)
    subprocess.Popen(["python", "KLLDestructCrasher.py"])
    subprocess.Popen(["python", "KLLDestructSplash.py"])
else:
    print("0")
