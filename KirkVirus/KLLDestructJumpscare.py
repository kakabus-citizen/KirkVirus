import tkinter as tk
from PIL import Image, ImageTk
import pygame
import random

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

    root.after(random.randint(500, 2000), hide_jumpscare)

def hide_jumpscare():
    root.withdraw()
    root.after(random.randint(10000, 10000), jumpscare)

root.after(random.randint(2000, 10000), jumpscare)

root.mainloop()