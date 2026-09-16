import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.overrideredirect(True)
root.config(bg="black")
root.wm_attributes("-transparentcolor", "black")
root.attributes("-topmost", True)

# Load PNG
original_image = Image.open("kirk.ico").convert("RGBA")

# Resize PNG to 300x300
original_image = original_image.resize((300, 300), Image.Resampling.LANCZOS)

label = tk.Label(root, bg="black", borderwidth=0)
label.pack()

angle = 0

def rotate():
    global angle

    angle = (angle + 9) % 360

    rotated = original_image.rotate(
        -angle,
        resample=Image.Resampling.BICUBIC,
        expand=False
    )

    photo = ImageTk.PhotoImage(rotated)
    label.config(image=photo)
    label.image = photo

    root.after(20, rotate)

# 300x300, bottom-left
screen_height = root.winfo_screenheight()
root.geometry(f"390x390+0+{screen_height - 390}")

rotate()
root.mainloop()