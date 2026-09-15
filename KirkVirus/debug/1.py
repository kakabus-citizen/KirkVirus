import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame

root = tk.Tk()

root.overrideredirect(True)
root.config(bg="black")
root.wm_attributes("-transparentcolor", "black")
root.attributes("-topmost", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+0+0")

canvas = tk.Canvas(
    root,
    width=screen_width,
    height=screen_height,
    bg="black",
    highlightthickness=0
)
canvas.pack()

# Load image
image = Image.open("kirk.ico").convert("RGBA")
image = image.resize((70, 70), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Grid spacing
spacing = 80

# Create every possible grid position
positions = []

for y in range(0, screen_height - 70, spacing):
    for x in range(0, screen_width - 70, spacing):
        positions.append((x, y))

# Randomize the order
random.shuffle(positions)

def smear():
    if positions:
        # Take one unused position
        x, y = positions.pop()

        # Place icon
        canvas.create_image(
            x,
            y,
            image=photo,
            anchor="nw"
        )

        # Do another one later
        root.after(10, smear)

    else:
        print("Grid completely filled!")

smear()

pygame.mixer.init()
pygame.mixer.music.load("fart1.mp3")
pygame.mixer.music.play(-1)

root.mainloop()