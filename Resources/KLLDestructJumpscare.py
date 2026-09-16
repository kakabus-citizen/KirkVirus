import tkinter as tk
from PIL import Image, ImageTk
import pygame
import random
from pycaw.pycaw import AudioUtilities


speakers = AudioUtilities.GetSpeakers()
volume = speakers.EndpointVolume

volume.SetMasterVolumeLevelScalar(0.5, None)

print("jumpscare v0.2 By Kaka")

pygame.mixer.init()

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(bg="black")

image = Image.open("jumpscare.ico")
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack(fill="both", expand=True)

root.withdraw()

def jumpscare():
    root.deiconify()
    pygame.mixer.music.load("jumpscare.mp3")
    pygame.mixer.music.play()

    root.after(random.randint(2000, 2000), hide_jumpscare)

def hide_jumpscare():
    root.withdraw()
    root.after(random.randint(10000, 10000), jumpscare)
    print("Executed")

root.after(random.randint(1000, 10000), jumpscare)


root.mainloop()