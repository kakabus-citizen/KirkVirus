import subprocess
import time
import webbrowser
time.sleep(3)

Url = "Note.html"

webbrowser.open_new_tab(Url)
time.sleep(4)

subprocess.Popen(["python", "KLLDestructVolumeMaxxer.py"])
subprocess.Popen(["python", "KLLTimer.py"])
print("timer")
subprocess.Popen(["python", "KLLRainbow.py"])
subprocess.Popen(["python", "KLLDestructAppearingKirksSmall-ish.py"])
print("sish")
time.sleep(1)
subprocess.Popen(["python", "KLLDestructAppearingKirksBig-ish.py"])
print("bish")
subprocess.Popen(["python", "KLLDestructKirkRotatingLogo.py"])
subprocess.Popen(["python", "KLLDestructZuckRotatingLogo.py"])
subprocess.Popen(["python", "KLLDestructIsraelRotatingLogo.py"])
print("logo")
subprocess.Popen(["python", "KLLDestructBouncingZuck.py"])
subprocess.Popen(["python", "KLLDestructBouncingKirk.py"])
subprocess.Popen(["python", "KLLDestructAudioPlayer.py"])
time.sleep(12)
subprocess.Popen(["python", "KLLDestructJumpscare.py"])